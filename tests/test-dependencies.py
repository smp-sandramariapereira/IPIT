import re
from collections import Counter, deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_PATH = SKILLS_DIR / "catalog.yaml"
EXPECTED_ROOT = "identificar-persona"
EXPECTED_SEQUENCE = [
    "identificar-persona",
    "orquestrar-ipit",
    "iniciar-ideathon",
    "conduzir-descoberta",
    "conduzir-ideacao",
    "desenhar-solucao",
    "selecionar-tecnologia",
    "definir-mvp",
    "planejar-arquitetura",
    "acompanhar-desenvolvimento",
    "preparar-pitch",
]

# Evidencias fornecidas pelo contexto humano ou institucional, e nao por uma
# skill anterior. Todos os demais itens de required-evidence devem ser
# rastreaveis a produces de algum ancestral no grafo.
EXTERNAL_EVIDENCE = {
    "contexto-inicial-da-turma",
    "restricoes-de-infraestrutura",
    "restricoes-de-tempo-e-infraestrutura",
}


def available_skill_names():
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def parse_catalog_entries():
    content = CATALOG_PATH.read_text(encoding="utf-8").splitlines()
    entries = []
    current = None
    in_dep_block = False

    for line in content:
        name_match = re.match(r"^  - name:\s*(\S+)\s*$", line)
        if name_match:
            current = {"name": name_match.group(1), "path": None, "depends_on": []}
            entries.append(current)
            in_dep_block = False
            continue

        if current is None:
            continue

        path_match = re.match(r"^\s{4}path:\s*(\S+)\s*$", line)
        if path_match:
            current["path"] = path_match.group(1)
            in_dep_block = False
            continue

        if re.match(r"^\s{4}depends_on:\s*\[\]\s*$", line):
            current["depends_on"] = []
            in_dep_block = False
            continue

        if re.match(r"^\s{4}depends_on:\s*$", line):
            current["depends_on"] = []
            in_dep_block = True
            continue

        if in_dep_block:
            dep_match = re.match(r"^\s{6}-\s*(\S+)\s*$", line)
            if dep_match:
                current["depends_on"].append(dep_match.group(1))
                continue
            in_dep_block = False

    return entries


def catalog_graph():
    return {entry["name"]: list(entry["depends_on"]) for entry in parse_catalog_entries()}


def extract_frontmatter(content):
    normalized = content.replace("\r\n", "\n")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", normalized, flags=re.DOTALL)
    assert match, "Frontmatter YAML ausente"
    return match.group(1)


def parse_frontmatter_list(skill_file: Path, key: str):
    frontmatter = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
    values = []
    in_block = False

    for line in frontmatter.splitlines():
        if re.match(rf"^\s*{re.escape(key)}:\s*\[\]\s*$", line):
            return []

        if re.match(rf"^\s*{re.escape(key)}:\s*$", line):
            in_block = True
            values = []
            continue

        if in_block:
            value_match = re.match(r"^\s+-\s*(\S+)\s*$", line)
            if value_match:
                values.append(value_match.group(1))
                continue

            if re.match(r"^\s*[a-zA-Z0-9_-]+:\s*", line):
                break

    return values


def parse_frontmatter_dependencies(skill_file: Path):
    return parse_frontmatter_list(skill_file, "depends-on")


def skill_contracts():
    contracts = {}
    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        contracts[skill_name] = {
            "depends_on": parse_frontmatter_list(skill_file, "depends-on"),
            "required_evidence": parse_frontmatter_list(
                skill_file, "required-evidence"
            ),
            "produces": parse_frontmatter_list(skill_file, "produces"),
        }
    return contracts


def find_cycle(graph):
    state = {name: 0 for name in graph}
    stack = []

    def visit(node):
        state[node] = 1
        stack.append(node)

        for dependency in graph[node]:
            if state[dependency] == 0:
                cycle = visit(dependency)
                if cycle:
                    return cycle
            elif state[dependency] == 1:
                start = stack.index(dependency)
                return stack[start:] + [dependency]

        stack.pop()
        state[node] = 2
        return None

    for node in graph:
        if state[node] == 0:
            cycle = visit(node)
            if cycle:
                return cycle

    return None


def reachable_from_root(graph, root):
    dependents = {name: [] for name in graph}
    for skill, dependencies in graph.items():
        for dependency in dependencies:
            dependents[dependency].append(skill)

    visited = set()
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(dependents[current])

    return visited


def ancestor_skills(graph, skill_name):
    ancestors = set()
    stack = list(graph[skill_name])

    while stack:
        current = stack.pop()
        if current in ancestors:
            continue
        ancestors.add(current)
        stack.extend(graph[current])

    return ancestors


def test_catalog_has_no_duplicate_skill_names():
    names = [entry["name"] for entry in parse_catalog_entries()]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    assert not duplicates, f"Skills duplicadas no catalogo: {duplicates}"


def test_catalog_and_workspace_have_same_skills():
    workspace = available_skill_names()
    catalog = set(catalog_graph())
    assert workspace == catalog, (
        f"Divergencia entre workspace e catalogo. "
        f"somente_workspace={sorted(workspace - catalog)} "
        f"somente_catalogo={sorted(catalog - workspace)}"
    )


def test_catalog_paths_are_unique_and_valid():
    entries = parse_catalog_entries()
    paths = [entry["path"] for entry in entries]
    duplicates = sorted(path for path, count in Counter(paths).items() if count > 1)
    assert None not in paths, "Skill sem path declarado no catalogo"
    assert not duplicates, f"Paths duplicados no catalogo: {duplicates}"

    for entry in entries:
        expected = f"skills/{entry['name']}/SKILL.md"
        assert entry["path"] == expected, (
            f"Path inconsistente para {entry['name']}: "
            f"declarado={entry['path']} esperado={expected}"
        )
        assert (ROOT / entry["path"]).is_file(), f"Arquivo ausente: {entry['path']}"


def test_dependency_targets_exist():
    graph = catalog_graph()
    catalog_skills = set(graph)

    for skill_name, dependencies in graph.items():
        for dependency in dependencies:
            assert dependency in catalog_skills, (
                f"Dependencia inexistente no catalogo: {skill_name} -> {dependency}"
            )


def test_dependencies_are_not_duplicated():
    for skill_name, dependencies in catalog_graph().items():
        duplicates = sorted(
            dependency
            for dependency, count in Counter(dependencies).items()
            if count > 1
        )
        assert not duplicates, (
            f"Dependencias duplicadas para {skill_name}: {duplicates}"
        )


def test_skills_do_not_depend_on_themselves():
    for skill_name, dependencies in catalog_graph().items():
        assert skill_name not in dependencies, f"Auto-dependencia: {skill_name}"


def test_dependency_graph_is_acyclic():
    graph = catalog_graph()
    cycle = find_cycle(graph)
    assert cycle is None, f"Ciclo de dependencias detectado: {' -> '.join(cycle)}"


def test_graph_has_single_expected_root():
    graph = catalog_graph()
    roots = sorted(name for name, dependencies in graph.items() if not dependencies)
    assert roots == [EXPECTED_ROOT], (
        f"Raizes inesperadas no grafo: {roots}; esperada={[EXPECTED_ROOT]}"
    )


def test_all_skills_are_reachable_from_root():
    graph = catalog_graph()
    assert EXPECTED_ROOT in graph, f"Raiz ausente: {EXPECTED_ROOT}"
    reachable = reachable_from_root(graph, EXPECTED_ROOT)
    unreachable = sorted(set(graph) - reachable)
    assert not unreachable, (
        f"Skills orfas ou desconectadas da raiz {EXPECTED_ROOT}: {unreachable}"
    )


def test_catalog_matches_official_ipit_sequence():
    entries = parse_catalog_entries()
    catalog_sequence = [entry["name"] for entry in entries]
    assert catalog_sequence == EXPECTED_SEQUENCE, (
        "Sequencia do catalogo diverge da jornada metodologica oficial do IPIT. "
        f"catalogo={catalog_sequence} esperada={EXPECTED_SEQUENCE}"
    )

    graph = catalog_graph()
    expected_graph = {EXPECTED_SEQUENCE[0]: []}
    for previous, current in zip(EXPECTED_SEQUENCE, EXPECTED_SEQUENCE[1:]):
        expected_graph[current] = [previous]

    assert graph == expected_graph, (
        "Dependencias do catalogo divergem da sequencia metodologica oficial do IPIT. "
        f"catalogo={graph} esperado={expected_graph}"
    )


def test_frontmatter_dependency_targets_exist():
    valid_skills = available_skill_names()

    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        dependencies = parse_frontmatter_dependencies(skill_file)
        for dependency in dependencies:
            assert dependency in valid_skills, (
                f"Dependencia inexistente no frontmatter: {skill_name} -> {dependency}"
            )


def test_catalog_and_frontmatter_dependencies_are_consistent():
    graph = catalog_graph()

    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        assert skill_name in graph, f"Skill ausente no catalogo: {skill_name}"
        frontmatter_dependencies = parse_frontmatter_dependencies(skill_file)
        assert frontmatter_dependencies == graph[skill_name], (
            f"Dependencias divergentes ou fora de ordem para {skill_name}. "
            f"frontmatter={frontmatter_dependencies} catalogo={graph[skill_name]}"
        )


def test_evidence_contracts_have_no_duplicates():
    for skill_name, contract in skill_contracts().items():
        for field in ("required_evidence", "produces"):
            values = contract[field]
            duplicates = sorted(
                value for value, count in Counter(values).items() if count > 1
            )
            assert not duplicates, (
                f"Valores duplicados em {field} de {skill_name}: {duplicates}"
            )


def test_required_evidence_is_available_from_ancestors_or_external_inputs():
    graph = catalog_graph()
    contracts = skill_contracts()

    for skill_name, contract in contracts.items():
        available = set(EXTERNAL_EVIDENCE)
        for ancestor in ancestor_skills(graph, skill_name):
            available.update(contracts[ancestor]["produces"])

        missing = sorted(set(contract["required_evidence"]) - available)
        assert not missing, (
            f"Evidencias sem origem rastreavel para {skill_name}: {missing}. "
            f"Disponiveis nos ancestrais ou contexto externo: {sorted(available)}"
        )


def test_each_dependency_edge_has_direct_semantic_handoff():
    graph = catalog_graph()
    contracts = skill_contracts()

    for skill_name, dependencies in graph.items():
        required = set(contracts[skill_name]["required_evidence"])
        for dependency in dependencies:
            direct_products = set(contracts[dependency]["produces"])
            handoff = sorted(required & direct_products)
            assert handoff, (
                f"Sem handoff semantico direto: {dependency} -> {skill_name}. "
                f"required-evidence={sorted(required)} "
                f"produces-da-dependencia={sorted(direct_products)}"
            )
