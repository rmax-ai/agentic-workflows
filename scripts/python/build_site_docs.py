from __future__ import annotations

import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "build" / "site-docs"

ONTOLOGY_DOCS = {
    Path("docs/ontology.md"): Path("ontology/ontology.md"),
    Path("docs/schema.md"): Path("ontology/schema.md"),
    Path("docs/index-tree.md"): Path("ontology/index-tree.md"),
    Path("docs/contribution-guide.md"): Path("ontology/contribution-guide.md"),
}

VIEW_DESTINATIONS = {
    "index-tree": Path("browse/index-tree.md"),
    "by-domain": Path("browse/by-domain.md"),
    "by-architecture": Path("browse/by-architecture.md"),
    "by-autonomy": Path("browse/by-autonomy.md"),
    "by-risk": Path("browse/by-risk.md"),
}


def reset_output_tree() -> None:
    if DOCS_ROOT.exists():
        shutil.rmtree(DOCS_ROOT)
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(read_text(path))


def relative_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_path.parent).replace(os.sep, "/")


def as_list(value: object) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def bool_text(value: object) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return "Unknown"


def bullet_lines(items: list[str], empty: str = "None.") -> list[str]:
    if not items:
        return [empty]
    return [f"- {item}" for item in items]


def label_id_text(data: dict | None) -> str:
    if not isinstance(data, dict):
        return "Unknown"
    label = data.get("label") or data.get("id") or "Unknown"
    identifier = data.get("id")
    if identifier and identifier != label:
        return f"{label} (`{identifier}`)"
    return str(label)


def compact_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return bool_text(value)
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        return ", ".join(f"{key}: {compact_text(inner)}" for key, inner in value.items() if inner not in (None, [], {}))
    if isinstance(value, list):
        return ", ".join(compact_text(item) for item in value if item not in (None, [], {}))
    return str(value)


def render_rich_list(items: list[dict], title_key: str, fields: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for item in items:
        title = item.get(title_key, "Untitled")
        lines.append(f"### {title}")
        for label, key in fields:
            value = item.get(key)
            if value in (None, [], {}):
                continue
            if isinstance(value, list):
                lines.append(f"- **{label}:**")
                lines.extend(f"  - {compact_text(entry)}" for entry in value)
            else:
                lines.append(f"- **{label}:** {compact_text(value)}")
        lines.append("")
    return lines


def make_pattern_page_path(pattern: dict) -> Path:
    family_id = pattern["pattern_family"]["id"]
    return Path("patterns") / family_id / f"{pattern['id']}.md"


def make_family_doc_dest(path: Path) -> Path:
    if path.name == "README.md":
        return Path("pattern-families/index.md")
    return Path("pattern-families") / path.name


def make_instance_dest(path: Path) -> Path:
    return Path("instances") / path.relative_to(ROOT / "instances")


def make_vocab_dest(path: Path) -> Path:
    return Path("vocabularies") / f"{path.stem}.md"


def build_source_map(patterns: list[dict], family_doc_paths: list[Path], instance_paths: list[Path], vocabulary_paths: list[Path]) -> dict[Path, Path]:
    source_map: dict[Path, Path] = {
        Path("README.md"): Path("index.md"),
        Path("schema/pattern.schema.json"): Path("schema/pattern.schema.json"),
    }
    source_map.update(ONTOLOGY_DOCS)
    for path in family_doc_paths:
        source_map[path.relative_to(ROOT)] = make_family_doc_dest(path)
    for path in instance_paths:
        source_map[path.relative_to(ROOT)] = make_instance_dest(path)
    for path in vocabulary_paths:
        source_map[path.relative_to(ROOT)] = make_vocab_dest(path)
    for pattern in patterns:
        source_map[pattern["_source_rel"]] = pattern["_page_path"]
    for view_name, dest in VIEW_DESTINATIONS.items():
        source_map[Path("data/views") / f"{view_name}.yaml"] = dest
    return source_map


LINK_PATTERN = re.compile(r"(!?\[[^\]]*\])\(([^)]+)\)")


def rewrite_links(text: str, source_rel: Path, dest_rel: Path, source_map: dict[Path, Path]) -> str:
    def replacer(match: re.Match[str]) -> str:
        label, target = match.groups()
        if label.startswith("!"):
            return match.group(0)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        if target.startswith("/"):
            return match.group(0)
        base, anchor = (target.split("#", 1) + [""])[:2]
        resolved = (source_rel.parent / base).resolve().relative_to(ROOT)
        target_rel = source_map.get(resolved)
        if target_rel is None:
            return match.group(0)
        new_target = relative_link(dest_rel, target_rel)
        if anchor:
            new_target = f"{new_target}#{anchor}"
        return f"{label}({new_target})"

    return LINK_PATTERN.sub(replacer, text)


def load_patterns() -> list[dict]:
    patterns: list[dict] = []
    for path in sorted((ROOT / "data/patterns").glob("*/*.yaml")):
        pattern = load_yaml(path)
        pattern["_source_path"] = path
        pattern["_source_rel"] = path.relative_to(ROOT)
        pattern["_page_path"] = make_pattern_page_path(pattern)
        patterns.append(pattern)
    return patterns


def load_vocabularies() -> dict[str, dict]:
    vocabularies: dict[str, dict] = {}
    for path in sorted((ROOT / "data/vocabularies").glob("*.yaml")):
        vocabulary = load_yaml(path)
        vocabulary["_source_path"] = path
        vocabulary["_source_rel"] = path.relative_to(ROOT)
        vocabulary["_page_path"] = make_vocab_dest(path)
        vocabularies[vocabulary["vocabulary"]] = vocabulary
    return vocabularies


def load_views() -> dict[str, dict]:
    views: dict[str, dict] = {}
    for path in sorted((ROOT / "data/views").glob("*.yaml")):
        view = load_yaml(path)
        view["_source_path"] = path
        view["_source_rel"] = path.relative_to(ROOT)
        view["_page_path"] = VIEW_DESTINATIONS[path.stem]
        views[view["view"]] = view
    return views


def extract_section(markdown: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def parse_linked_patterns(markdown: str) -> list[str]:
    section = extract_section(markdown, "Linked pattern(s)")
    return re.findall(r"`([^`]+)`", section)


def parse_instance_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def parse_instance_summary(markdown: str) -> str:
    summary = extract_section(markdown, "Scenario summary")
    return " ".join(line.strip() for line in summary.splitlines() if line.strip())


def load_instances() -> list[dict]:
    instances: list[dict] = []
    for path in sorted((ROOT / "instances").glob("*/*.md")):
        markdown = read_text(path)
        instances.append(
            {
                "title": parse_instance_title(markdown, path.stem.replace("-", " ").title()),
                "summary": parse_instance_summary(markdown),
                "linked_patterns": parse_linked_patterns(markdown),
                "domain": path.parent.name,
                "source_path": path,
                "source_rel": path.relative_to(ROOT),
                "page_path": make_instance_dest(path),
                "content": markdown,
            }
        )
    return instances


def build_pattern_usage_maps(patterns: list[dict]) -> dict[str, dict[str, list[dict]]]:
    usage: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for pattern in patterns:
        usage["problem-structures"][pattern["problem_structure"]["id"]].append(pattern)
        for domain in pattern.get("domain", []):
            usage["domains"][domain["id"]].append(pattern)
        for entry in pattern.get("execution_architecture", []):
            usage["architectures"][entry["architecture"]["id"]].append(pattern)
        for entry in pattern.get("capability_requirements", []):
            usage["capabilities"][entry["capability"]["id"]].append(pattern)
        autonomy = pattern.get("autonomy_profile", {}).get("level", {})
        if autonomy.get("id"):
            usage["autonomy-levels"][autonomy["id"]].append(pattern)
        risk = pattern.get("risk_governance", {}).get("level", {})
        if risk.get("id"):
            usage["risk-levels"][risk["id"]].append(pattern)
    return usage


def render_home(source_map: dict[Path, Path]) -> None:
    source_rel = Path("README.md")
    dest_rel = Path("index.md")
    content = rewrite_links(read_text(ROOT / source_rel), source_rel, dest_rel, source_map)
    write_text(DOCS_ROOT / dest_rel, content)


def render_ontology_pages(source_map: dict[Path, Path]) -> None:
    index_lines = [
        "# Ontology",
        "",
        "The ontology layer explains how the repository is organized, authored, and validated.",
        "",
        "## Foundations",
        "",
        "- [Ontology model](ontology.md)",
        "- [Schema guide](schema.md)",
        "- [Browse tree](index-tree.md)",
        "- [Contribution guide](contribution-guide.md)",
    ]
    write_text(DOCS_ROOT / "ontology/index.md", "\n".join(index_lines))
    for source_rel, dest_rel in ONTOLOGY_DOCS.items():
        content = rewrite_links(read_text(ROOT / source_rel), source_rel, dest_rel, source_map)
        write_text(DOCS_ROOT / dest_rel, content)


def render_family_pages(patterns: list[dict], source_map: dict[Path, Path]) -> None:
    family_docs = sorted((ROOT / "docs/patterns").glob("*.md"))
    patterns_by_family: dict[str, list[dict]] = defaultdict(list)
    for pattern in patterns:
        patterns_by_family[pattern["pattern_family"]["id"]].append(pattern)

    readme_source = Path("docs/patterns/README.md")
    readme_dest = Path("pattern-families/index.md")
    readme_text = rewrite_links(read_text(ROOT / readme_source), readme_source, readme_dest, source_map)
    extra_lines = ["", "## Canonical families", ""]
    for path in sorted(family_docs):
        if path.name == "README.md":
            continue
        family_id = path.stem
        count = len(patterns_by_family[family_id])
        extra_lines.append(f"- [{family_id}]({path.name}) ({count} canonical patterns)")
    write_text(DOCS_ROOT / readme_dest, readme_text + "\n" + "\n".join(extra_lines))

    for path in family_docs:
        if path.name == "README.md":
            continue
        source_rel = path.relative_to(ROOT)
        dest_rel = make_family_doc_dest(path)
        family_id = path.stem
        content = rewrite_links(read_text(path), source_rel, dest_rel, source_map)
        appended = ["", "## Canonical patterns in this family", ""]
        for pattern in patterns_by_family[family_id]:
            appended.append(
                f"- [{pattern['name']}]({relative_link(dest_rel, pattern['_page_path'])})"
            )
        write_text(DOCS_ROOT / dest_rel, content + "\n" + "\n".join(appended))


def render_pattern_indexes(patterns: list[dict], views: dict[str, dict]) -> None:
    families = views["index-tree"]["families"]
    index_lines = [
        "# Patterns",
        "",
        "Canonical pattern reference pages are generated from `data/patterns/` and remain the publication-friendly view of the YAML source of truth.",
        "",
        "## Families",
        "",
    ]
    for family_entry in families:
        family_id = family_entry["family"]["id"]
        family_patterns = [pattern for pattern in patterns if pattern["pattern_family"]["id"] == family_id]
        family_index = Path("patterns") / family_id / "index.md"
        index_lines.append(f"- [{family_id}]({relative_link(Path('patterns/index.md'), family_index)}) ({len(family_patterns)} patterns)")
        family_lines = [
            f"# {family_id}",
            "",
            f"Pattern family reference for `{family_id}`.",
            "",
            "## Canonical patterns",
            "",
        ]
        for pattern in family_patterns:
            family_lines.append(f"- [{pattern['name']}]({pattern['id']}.md)")
        write_text(DOCS_ROOT / family_index, "\n".join(family_lines))
    write_text(DOCS_ROOT / "patterns/index.md", "\n".join(index_lines))


def render_pattern_pages(patterns: list[dict], instances: list[dict], source_map: dict[Path, Path]) -> None:
    instances_by_pattern: dict[str, list[dict]] = defaultdict(list)
    for instance in instances:
        for pattern_id in instance["linked_patterns"]:
            instances_by_pattern[pattern_id].append(instance)

    pattern_lookup = {pattern["id"]: pattern for pattern in patterns}

    for pattern in patterns:
        dest_rel = pattern["_page_path"]
        family_link = relative_link(dest_rel, Path("pattern-families") / f"{pattern['pattern_family']['id']}.md")
        lines = [
            f"# {pattern['name']}",
            "",
            pattern["summary"],
            "",
            "## Metadata",
            "",
            f"- **Pattern id:** `{pattern['id']}`",
            f"- **Pattern family:** [{pattern['pattern_family']['label']}]({family_link})",
            f"- **Problem structure:** {label_id_text(pattern.get('problem_structure'))}",
            f"- **Domains:** {', '.join(label_id_text(entry) for entry in pattern.get('domain', [])) or 'None'}",
            "",
            "## Workflow goal",
            "",
            pattern.get("workflow_goal", ""),
            "",
            "## Inputs",
            "",
        ]
        lines.extend(
            render_rich_list(
                pattern.get("inputs", []),
                "name",
                [
                    ("Description", "description"),
                    ("Kind", "kind"),
                    ("Required", "required"),
                    ("Examples", "examples"),
                ],
            )
            or ["None.", ""]
        )
        lines.extend(["## Outputs", ""])
        lines.extend(
            render_rich_list(
                pattern.get("outputs", []),
                "name",
                [
                    ("Description", "description"),
                    ("Kind", "kind"),
                    ("Required", "required"),
                    ("Examples", "examples"),
                ],
            )
            or ["None.", ""]
        )

        environment = pattern.get("environment", {})
        lines.extend(
            [
                "## Environment",
                "",
                environment.get("summary", ""),
                "",
                "### Systems",
                "",
                *bullet_lines(environment.get("systems", [])),
                "",
                "### Actors",
                "",
                *bullet_lines(environment.get("actors", [])),
                "",
                "### Constraints",
                "",
                *bullet_lines(environment.get("constraints", [])),
                "",
                "### Assumptions",
                "",
                *bullet_lines(environment.get("assumptions", [])),
                "",
                "## Capability requirements",
                "",
            ]
        )

        for requirement in pattern.get("capability_requirements", []):
            capability = requirement.get("capability", {})
            lines.append(f"- **{label_id_text(capability)}:** {requirement.get('necessity', '')}")
        if not pattern.get("capability_requirements"):
            lines.append("None.")

        lines.extend(["", "## Execution architecture", ""])
        for entry in pattern.get("execution_architecture", []):
            architecture = entry.get("architecture", {})
            lines.append(f"- **{label_id_text(architecture)}:** {entry.get('fit', '')}")
        if not pattern.get("execution_architecture"):
            lines.append("None.")

        autonomy = pattern.get("autonomy_profile", {})
        lines.extend(
            [
                "",
                "## Autonomy profile",
                "",
                f"- **Level:** {label_id_text(autonomy.get('level'))}",
                f"- **Reversibility:** {autonomy.get('reversibility', 'Not specified.')}",
                f"- **Escalation:** {autonomy.get('escalation', 'Not specified.')}",
                "",
                "### Human checkpoints",
                "",
                *bullet_lines(autonomy.get("human_checkpoints", [])),
                "",
            ]
        )

        risk = pattern.get("risk_governance", {})
        lines.extend(
            [
                "## Risk and governance",
                "",
                f"- **Risk level:** {label_id_text(risk.get('level'))}",
                f"- **Failure impact:** {risk.get('failure_impact', 'Not specified.')}",
                f"- **Auditability:** {risk.get('auditability', 'Not specified.')}",
                "",
                "### Approval requirements",
                "",
                *bullet_lines(risk.get("approval_requirements", [])),
                "",
                "### Privacy",
                "",
                *bullet_lines(risk.get("privacy", [])),
                "",
                "### Security",
                "",
                *bullet_lines(risk.get("security", [])),
            ]
        )
        if risk.get("notes"):
            lines.extend(["", f"**Notes:** {risk['notes']}"])

        lines.extend(["", "## Why agentic", ""])
        lines.extend(bullet_lines(pattern.get("why_agentic", [])))

        lines.extend(["", "## Failure modes", ""])
        failure_modes = pattern.get("failure_modes", [])
        if failure_modes:
            for failure_mode in failure_modes:
                lines.extend(
                    [
                        f"### {failure_mode.get('mode', 'Failure mode')}",
                        f"- **Impact:** {failure_mode.get('impact', '')}",
                        f"- **Severity:** {failure_mode.get('severity', '')}",
                        f"- **Detectability:** {failure_mode.get('detectability', '')}",
                        "- **Mitigations:**",
                        *[f"  - {item}" for item in failure_mode.get("mitigations", [])],
                        "",
                    ]
                )
        else:
            lines.append("None.")

        evaluation = pattern.get("evaluation", {})
        lines.extend(
            [
                "## Evaluation",
                "",
                "### Success metrics",
                "",
                *bullet_lines(evaluation.get("success_metrics", [])),
                "",
                "### Quality criteria",
                "",
                *bullet_lines(evaluation.get("quality_criteria", [])),
                "",
                "### Robustness checks",
                "",
                *bullet_lines(evaluation.get("robustness_checks", [])),
            ]
        )
        if evaluation.get("benchmark_notes"):
            lines.extend(["", f"**Benchmark notes:** {evaluation['benchmark_notes']}"])

        implementation = pattern.get("implementation_notes", {})
        lines.extend(
            [
                "",
                "## Implementation notes",
                "",
                "### Orchestration notes",
                "",
                *bullet_lines(implementation.get("orchestration_notes", [])),
                "",
                "### Integration notes",
                "",
                *bullet_lines(implementation.get("integration_notes", [])),
                "",
                "### Deployment notes",
                "",
                *bullet_lines(implementation.get("deployment_notes", [])),
            ]
        )
        references = implementation.get("references", [])
        if references:
            lines.extend(["", "### References", ""])
            for reference in references:
                reference_path = Path(reference)
                dest = source_map.get(reference_path)
                if dest is None:
                    lines.append(f"- `{reference}`")
                    continue
                lines.append(f"- [{reference}]({relative_link(dest_rel, dest)})")

        lines.extend(["", "## Example domains", ""])
        example_domains = pattern.get("example_domains", [])
        if example_domains:
            for example_domain in example_domains:
                domain = example_domain.get("domain", {})
                lines.append(f"- **{label_id_text(domain)}:** {example_domain.get('example', '')}")
        else:
            lines.append("None.")

        lines.extend(["", "## Related patterns", ""])
        related_patterns = pattern.get("related_patterns", [])
        if related_patterns:
            for related in related_patterns:
                related_pattern = pattern_lookup.get(related.get("id"))
                if related_pattern is not None:
                    link = relative_link(dest_rel, related_pattern["_page_path"])
                    title = related_pattern["name"]
                    lines.append(f"- [{title}]({link}) ({related.get('relationship', 'related')})")
                else:
                    lines.append(f"- `{related.get('id', 'unknown')}` ({related.get('relationship', 'related')})")
                if related.get("notes"):
                    lines.append(f"  - {related['notes']}")
        else:
            lines.append("None.")

        lines.extend(["", "## Grounded instances", ""])
        linked_instances = instances_by_pattern.get(pattern["id"], [])
        if linked_instances:
            for instance in linked_instances:
                lines.append(
                    f"- [{instance['title']}]({relative_link(dest_rel, instance['page_path'])})"
                )
        else:
            lines.append("None yet.")

        lines.extend(
            [
                "",
                "## Canonical source",
                "",
                f"- `{pattern['_source_rel'].as_posix()}`",
            ]
        )
        write_text(DOCS_ROOT / dest_rel, "\n".join(lines))


def render_index_tree(view: dict, patterns: list[dict]) -> None:
    pattern_lookup = {pattern["id"]: pattern for pattern in patterns}
    lines = [
        f"# {view['title']}",
        "",
        view.get("summary", ""),
        "",
        "This page is a derived browse artifact generated from canonical repository data.",
        "",
    ]
    root = view.get("root", {})
    if root:
        lines.extend([f"- **Root:** {root.get('label', root.get('id', 'Patterns'))}", f"- **Summary:** {root.get('summary', '')}", ""])
    lines.extend(["## Families", ""])
    for family_entry in view.get("families", []):
        family_id = family_entry["family"]["id"]
        family_index = Path("patterns") / family_id / "index.md"
        lines.append(f"### [{family_id}]({relative_link(view['_page_path'], family_index)})")
        related = family_entry.get("related_problem_structures", [])
        if related:
            lines.append(f"- **Problem structures:** {', '.join(label_id_text(item) for item in related)}")
        pattern_ids = family_entry.get("pattern_ids", [])
        if pattern_ids:
            lines.append("- **Patterns:**")
            for pattern_id in pattern_ids:
                pattern = pattern_lookup.get(pattern_id)
                if pattern is None:
                    continue
                lines.append(
                    f"  - [{pattern['name']}]({relative_link(view['_page_path'], pattern['_page_path'])})"
                )
        else:
            lines.append("- **Patterns:** None yet.")
        lines.append("")
    write_text(DOCS_ROOT / view["_page_path"], "\n".join(lines))


def render_grouped_view(view: dict, patterns: list[dict]) -> None:
    pattern_lookup = {pattern["id"]: pattern for pattern in patterns}
    group_key = next(
        key for key in ("domains", "architectures", "autonomy_levels", "risk_levels") if key in view
    )
    item_key = {
        "domains": "domain",
        "architectures": "architecture",
        "autonomy_levels": "autonomy_level",
        "risk_levels": "risk_level",
    }[group_key]
    lines = [
        f"# {view['title']}",
        "",
        view.get("summary", ""),
        "",
        "This page is a derived browse artifact generated from canonical repository data.",
        "",
    ]
    for note in view.get("usage_notes", []):
        lines.append(f"- {note}")
    lines.extend(["", "## Buckets", ""])
    for bucket in view.get(group_key, []):
        term = bucket[item_key]
        lines.append(f"### {label_id_text(term)}")
        pattern_families = bucket.get("pattern_families", {})
        for family_id, pattern_ids in pattern_families.items():
            if not pattern_ids:
                continue
            lines.append(f"- **{family_id}:**")
            for pattern_id in pattern_ids:
                pattern = pattern_lookup.get(pattern_id)
                if pattern is None:
                    continue
                lines.append(
                    f"  - [{pattern['name']}]({relative_link(view['_page_path'], pattern['_page_path'])})"
                )
        lines.append("")
    write_text(DOCS_ROOT / view["_page_path"], "\n".join(lines))


def render_browse_pages(views: dict[str, dict], patterns: list[dict]) -> None:
    index_lines = [
        "# Browse",
        "",
        "Derived browse pages expose the ontology through alternate navigation paths while keeping canonical pattern data in `data/patterns/`.",
        "",
        "## Views",
        "",
        "- [Pattern-first browse tree](index-tree.md)",
        "- [Browse by domain](by-domain.md)",
        "- [Browse by architecture](by-architecture.md)",
        "- [Browse by autonomy](by-autonomy.md)",
        "- [Browse by risk](by-risk.md)",
    ]
    write_text(DOCS_ROOT / "browse/index.md", "\n".join(index_lines))
    render_index_tree(views["index-tree"], patterns)
    for view_name in ("by-domain", "by-architecture", "by-autonomy", "by-risk"):
        render_grouped_view(views[view_name], patterns)


def inject_instance_links(instance: dict, patterns: list[dict]) -> str:
    pattern_lookup = {pattern["id"]: pattern for pattern in patterns}
    title_match = re.match(r"^(# .+?\n)(\n)?", instance["content"], re.DOTALL)
    if not title_match:
        return instance["content"]
    title_block = title_match.group(1).rstrip()
    rest = instance["content"][title_match.end() :].lstrip("\n")
    link_items = []
    for pattern_id in instance["linked_patterns"]:
        pattern = pattern_lookup.get(pattern_id)
        if pattern is None:
            continue
        link_items.append(
            f"[{pattern['name']}]({relative_link(instance['page_path'], pattern['_page_path'])})"
        )
    note_lines = [
        "> Canonical pattern(s): " + (", ".join(link_items) if link_items else "None recorded."),
        f"> Source Markdown: `{instance['source_rel'].as_posix()}`",
        "",
    ]
    return "\n".join([title_block, "", *note_lines, rest.strip()])


def render_instance_pages(instances: list[dict], patterns: list[dict]) -> None:
    instances_by_domain: dict[str, list[dict]] = defaultdict(list)
    instances_by_pattern: dict[str, list[dict]] = defaultdict(list)
    pattern_lookup = {pattern["id"]: pattern for pattern in patterns}
    for instance in instances:
        instances_by_domain[instance["domain"]].append(instance)
        for pattern_id in instance["linked_patterns"]:
            instances_by_pattern[pattern_id].append(instance)
        content = inject_instance_links(instance, patterns)
        write_text(DOCS_ROOT / instance["page_path"], content)

    index_lines = [
        "# Instances",
        "",
        "Grounded instances remain Markdown source documents in `instances/`, with this derived site layer adding browse indexes and canonical pattern backlinks.",
        "",
        "## Browse by domain",
        "",
    ]
    for domain in sorted(instances_by_domain):
        domain_index = Path("instances") / domain / "index.md"
        index_lines.append(f"- [{domain}]({relative_link(Path('instances/index.md'), domain_index)}) ({len(instances_by_domain[domain])} instances)")
        domain_lines = [f"# {domain}", "", f"Grounded examples for the `{domain}` domain.", "", "## Instances", ""]
        for instance in instances_by_domain[domain]:
            domain_lines.append(f"- [{instance['title']}]({instance['source_path'].name})")
            if instance["summary"]:
                domain_lines.append(f"  - {instance['summary']}")
        write_text(DOCS_ROOT / domain_index, "\n".join(domain_lines))
    index_lines.extend(["", "## Browse by pattern", "", "- [Instances by linked pattern](by-pattern.md)"])
    write_text(DOCS_ROOT / "instances/index.md", "\n".join(index_lines))

    by_pattern_lines = [
        "# Instances by linked pattern",
        "",
        "This index groups grounded examples by the canonical pattern they instantiate.",
        "",
    ]
    for pattern in patterns:
        linked_instances = instances_by_pattern.get(pattern["id"], [])
        if not linked_instances:
            continue
        by_pattern_lines.append(
            f"## [{pattern['name']}]({relative_link(Path('instances/by-pattern.md'), pattern['_page_path'])})"
        )
        for instance in linked_instances:
            by_pattern_lines.append(
                f"- [{instance['title']}]({relative_link(Path('instances/by-pattern.md'), instance['page_path'])})"
            )
        by_pattern_lines.append("")
    write_text(DOCS_ROOT / "instances/by-pattern.md", "\n".join(by_pattern_lines))


def render_vocabulary_pages(vocabularies: dict[str, dict], usage_map: dict[str, dict[str, list[dict]]]) -> None:
    index_lines = [
        "# Vocabularies",
        "",
        "Controlled vocabularies remain canonical YAML under `data/vocabularies/`; these pages publish their stable ids, guidance, and current pattern usage.",
        "",
        "## Vocabulary reference",
        "",
    ]
    for name, vocabulary in sorted(vocabularies.items()):
        index_lines.append(f"- [{vocabulary['title']}]({vocabulary['_page_path'].name})")
        lines = [
            f"# {vocabulary['title']}",
            "",
            vocabulary.get("summary", ""),
            "",
            "## Source fields",
            "",
            *bullet_lines(vocabulary.get("source_fields", [])),
            "",
            "## Usage notes",
            "",
            *bullet_lines(vocabulary.get("usage_notes", [])),
            "",
            "## Terms",
            "",
        ]
        for term in vocabulary.get("terms", []):
            lines.append(f"### {term.get('label', term.get('id', 'Term'))}")
            lines.append(f"- **Stable id:** `{term.get('id', '')}`")
            if term.get("summary"):
                lines.append(f"- **Summary:** {term['summary']}")
            if term.get("definition"):
                lines.append(f"- **Definition:** {term['definition']}")
            if term.get("selection_guidance"):
                lines.append(f"- **Selection guidance:** {term['selection_guidance']}")
            related = term.get("related_ids", [])
            if related:
                lines.append(f"- **Related ids:** {', '.join(f'`{item}`' for item in related)}")
            used_by = usage_map.get(name, {}).get(term.get("id", ""), [])
            if used_by:
                lines.append("- **Used by patterns:**")
                for pattern in used_by:
                    lines.append(
                        f"  - [{pattern['name']}]({relative_link(vocabulary['_page_path'], pattern['_page_path'])})"
                    )
            lines.append("")
        lines.extend(["## Canonical source", "", f"- `{vocabulary['_source_rel'].as_posix()}`"])
        write_text(DOCS_ROOT / vocabulary["_page_path"], "\n".join(lines))
    write_text(DOCS_ROOT / "vocabularies/index.md", "\n".join(index_lines))


def render_schema_pages(source_map: dict[Path, Path]) -> None:
    source_rel = Path("schema/pattern.schema.json")
    schema_json = ROOT / source_rel
    write_text(DOCS_ROOT / source_map[source_rel], read_text(schema_json))
    schema = json.loads(read_text(schema_json))
    properties = schema.get("properties", {})
    index_lines = [
        "# Schema",
        "",
        "The structural contract for canonical pattern YAML lives in the JSON Schema below.",
        "",
        "## Reference",
        "",
        "- [Schema guide](../ontology/schema.md)",
        "- [Raw JSON Schema](pattern.schema.json)",
        "",
        "## Top-level properties",
        "",
    ]
    for name, definition in properties.items():
        line = f"- **{name}:** {definition.get('description', 'No description provided.')}"
        index_lines.append(line)
    write_text(DOCS_ROOT / "schema/index.md", "\n".join(index_lines))


def main() -> None:
    patterns = load_patterns()
    vocabularies = load_vocabularies()
    views = load_views()
    instances = load_instances()

    family_doc_paths = sorted((ROOT / "docs/patterns").glob("*.md"))
    instance_paths = sorted((ROOT / "instances").glob("*/*.md"))
    vocabulary_paths = sorted((ROOT / "data/vocabularies").glob("*.yaml"))
    source_map = build_source_map(patterns, family_doc_paths, instance_paths, vocabulary_paths)

    reset_output_tree()
    render_home(source_map)
    render_ontology_pages(source_map)
    render_family_pages(patterns, source_map)
    render_pattern_indexes(patterns, views)
    render_pattern_pages(patterns, instances, source_map)
    render_browse_pages(views, patterns)
    render_instance_pages(instances, patterns)
    render_vocabulary_pages(vocabularies, build_pattern_usage_maps(patterns))
    render_schema_pages(source_map)


if __name__ == "__main__":
    main()
