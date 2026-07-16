from collections import Counter, deque
from pathlib import Path
from typing import Any

import yaml


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


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise AssertionError(f"YAML invalido em {path.relative_to(ROOT)}: {exc}") from exc

    assert isinstance(loaded, dict), (
        f"Documento YAML deve ser um objeto em {path.relative_to(ROOT)}"
    )
    return loaded


def available_skill_names() -> set[str]:
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def parse_catalog_entries() -> list[dict[str, Any]]:
    catalog = load_yaml_mapping(CATALOG_PATH)
    entries = catalog.get("skills")
    assert isinstance(entries, list), "skills deve ser uma lista em skills/catalog.yaml"

    normalized: list[dict[str, Any]] = []
    for index, entry in enumerate(entries, start=1):
        assert isinstance(entry, dict), f"Entrada #{index} do catalogo deve ser objeto"
        name = entry.get("name")
        path = entry.get("path")
        dependencies = entry.get("depends_on", [])
        assert isinstance(name, str) and name, f"Entrada #{index} sem name valido"
        assert isinstance(path, str) and path, f"Skill {name} sem path valido"
        assert isinstance(dependencies, list), f"depends_on de {name} deve ser lista"
        assert all(isinstance(dep, str) and dep for dep in dependencies), (
            f"depends_on de {name} contem valor invalido"
        )
        normalized.append(
            {"name": name, "path": path, "depends_on": list(dependencies)}
        )
    return normalized


def catalog_graph() -> dict[str, list[str]]:
    return {entry["name"]: list(entry["depends_on"]) for entry in parse_catalog_entries()}


def extract_frontmatter_text(content: str, skill_file: Path) -> str:
    normalized = content.replace("\r\n", "\n")
    lines = normalized.splitlines()
    assert lines and lines[0] == "---", (
        f"Frontmatter YAML ausente em {skill_file.relative_to(ROOT)}"
    )
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise AssertionError(
            f"Delimitador final do frontmatter ausente em {skill_file.relative_to(ROOT)}"
        ) from exc
    return "\n".join(lines[1:end])


def load_skill_frontmatter(skill_file: Path) -> dict[str, Any]:
    frontmatter_text = extract_frontmatter_text(
        skill_file.read_text(encoding="utf-8"), skill_file
    )
    try:
        loaded = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        raise AssertionError(
            f"Frontmatter YAML invalido em {skill_file.relative_to(ROOT)}: {exc}"
        ) from exc

    assert isinstance(loaded, dict), (
        f"Frontmatter deve ser objeto em {skill_file.relative_to(ROOT)}"
    )
    return loaded


def metadata_list(frontmatter: dict[str, Any], skill_name: str, key: str) -> list[str]:
    metadata = frontmatter.get("metadata")
    assert isinstance(metadata, dict), f"metadata ausente ou invalido em {skill_name}"
    values = metadata.get(key)
    assert isinstance(values, list), f"metadata.{key} deve ser lista em {skill_name}"
    assert all(isinstance(value, str) and value for value in values), (
        f"metadata.{key} contem valor invalido em {skill_name}"
    )
    return list(values)


def skill_contracts() -> dict[str, dict[str, list[str]]]:
    contracts: dict[str, dict[str, list[str]]] = {}
    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        frontmatter = load_skill_frontmatter(skill_file)
        declared_name = frontmatter.get("name")
        assert declared_name == skill_name, (
            f"name do frontmatter diverge da pasta: {declared_name!r} != {skill_name!r}"
        )
        contracts[skill_name] = {
            "depends_on": metadata_list(frontmatter, skill_name, "depends-on"),
            "required_evidence": metadata_list(
                frontmatter, skill_name, "required-evidence"
            ),
            "produces": metadata_list(frontmatter, skill_name, "produces"),
        }
    return contracts


def find_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    state = {name: 0 for name in graph}
    stack: list[str] = []

    def visit(node: str) -> list[str] | None:
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


def reachable_from_root(graph: dict[str, list[str]], root: str) -> set[str]:
    dependents = {name: [] for name in graph}
    for skill, dependencies in graph.items():
        for dependency in dependencies:
            dependents[dependency].append(skill)

    visited: set[str] = set()
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(dependents[current])
    return visited


def ancestor_skills(graph: dict[str, list[str]], skill_name: str) -> set[str]:
    ancestors: set[str] = set()
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
        "Divergencia entre workspace e catalogo. "
        f"somente_workspace={sorted(workspace - catalog)} "
        f"somente_catalogo={sorted(catalog - workspace)}"
    )


def test_catalog_paths_are_unique_and_valid():
    entries = parse_catalog_entries()
    paths = [entry["path"] for entry in entries]
    duplicates = sorted(path for path, count in Counter(paths).items() if count > 1)
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
        assert not duplicates, f"Dependencias duplicadas para {skill_name}: {duplicates}"


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
    unreachable = sorted(set(graph) - reachable_from_root(graph, EXPECTED_ROOT))
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

    expected_graph = {EXPECTED_SEQUENCE[0]: []}
    for previous, current in zip(EXPECTED_SEQUENCE, EXPECTED_SEQUENCE[1:]):
        expected_graph[current] = [previous]
    graph = catalog_graph()
    assert graph == expected_graph, (
        "Dependencias do catalogo divergem da sequencia metodologica oficial do IPIT. "
        f"catalogo={graph} esperado={expected_graph}"
    )


def test_frontmatter_dependency_targets_exist():
    valid_skills = available_skill_names()
    for skill_name, contract in skill_contracts().items():
        for dependency in contract["depends_on"]:
            assert dependency in valid_skills, (
                f"Dependencia inexistente no frontmatter: {skill_name} -> {dependency}"
            )


def test_catalog_and_frontmatter_dependencies_are_consistent():
    graph = catalog_graph()
    for skill_name, contract in skill_contracts().items():
        assert skill_name in graph, f"Skill ausente no catalogo: {skill_name}"
        assert contract["depends_on"] == graph[skill_name], (
            f"Dependencias divergentes ou fora de ordem para {skill_name}. "
            f"frontmatter={contract['depends_on']} catalogo={graph[skill_name]}"
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
