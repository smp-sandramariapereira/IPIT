import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_PATH = SKILLS_DIR / "catalog.yaml"


def available_skill_names():
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def parse_catalog_dependencies():
    content = CATALOG_PATH.read_text(encoding="utf-8").splitlines()
    dependencies = {}
    current_skill = None
    in_dep_block = False

    for line in content:
        name_match = re.match(r"^  - name:\s*(\S+)\s*$", line)
        if name_match:
            current_skill = name_match.group(1)
            dependencies[current_skill] = []
            in_dep_block = False
            continue

        if current_skill is None:
            continue

        if re.match(r"^\s{4}depends_on:\s*\[\]\s*$", line):
            dependencies[current_skill] = []
            in_dep_block = False
            continue

        if re.match(r"^\s{4}depends_on:\s*$", line):
            in_dep_block = True
            dependencies[current_skill] = []
            continue

        if in_dep_block:
            dep_match = re.match(r"^\s{6}-\s*(\S+)\s*$", line)
            if dep_match:
                dependencies[current_skill].append(dep_match.group(1))
                continue

            # End of dependency block when list indentation stops.
            in_dep_block = False

    return dependencies


def extract_frontmatter(content):
    match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
    assert match, "Frontmatter YAML ausente"
    return match.group(1)


def parse_frontmatter_dependencies(skill_file: Path):
    frontmatter = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
    lines = frontmatter.splitlines()

    deps = []
    in_dep_block = False

    for line in lines:
        if re.match(r"^\s*depends-on:\s*\[\]\s*$", line):
            return []

        if re.match(r"^\s*depends-on:\s*$", line):
            in_dep_block = True
            deps = []
            continue

        if in_dep_block:
            dep_match = re.match(r"^\s+-\s*(\S+)\s*$", line)
            if dep_match:
                deps.append(dep_match.group(1))
                continue

            if re.match(r"^\s*[a-zA-Z0-9_-]+:\s*", line):
                break

    return deps


def test_catalog_skills_exist_in_workspace():
    valid_skills = available_skill_names()
    catalog_deps = parse_catalog_dependencies()
    for skill_name in catalog_deps:
        assert skill_name in valid_skills, f"Skill declarada no catalogo nao existe: {skill_name}"


def test_catalog_dependency_targets_exist():
    catalog_deps = parse_catalog_dependencies()
    catalog_skills = set(catalog_deps.keys())

    for skill_name, deps in catalog_deps.items():
        for dep in deps:
            assert dep in catalog_skills, f"Dependencia inexistente no catalogo: {skill_name} -> {dep}"


def test_skill_frontmatter_dependency_targets_exist():
    valid_skills = available_skill_names()

    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        deps = parse_frontmatter_dependencies(skill_file)
        for dep in deps:
            assert dep in valid_skills, f"Dependencia inexistente no frontmatter: {skill_name} -> {dep}"


def test_catalog_and_frontmatter_dependencies_are_consistent():
    catalog_deps = parse_catalog_dependencies()

    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        assert skill_name in catalog_deps, f"Skill ausente no catalogo: {skill_name}"

        fm_deps = set(parse_frontmatter_dependencies(skill_file))
        cat_deps = set(catalog_deps[skill_name])
        assert fm_deps == cat_deps, (
            f"Dependencias divergentes para {skill_name}. "
            f"frontmatter={sorted(fm_deps)} catalogo={sorted(cat_deps)}"
        )
