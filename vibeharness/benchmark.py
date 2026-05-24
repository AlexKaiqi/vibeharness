"""Benchmark manifest validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple


REQUIRED_TOP_LEVEL = {
    "task_id",
    "title",
    "repo",
    "transfer_group",
    "user_request",
    "harness_gap",
    "harness_components",
    "observability",
    "intervention_trace",
    "decision_contract",
    "safety_constraints",
    "allowed_harness_edits",
    "visible_checks",
    "hidden_checks",
    "replay_protocol",
    "episode_package",
}

VALID_CLASSES = {
    "environment_bootstrap",
    "tool_affordance",
    "verification_blind_spot",
    "state_drift",
    "spec_capture",
    "coordination_breakdown",
}

VALID_COMPONENTS = {
    "task_specification",
    "context_selection",
    "tool_access",
    "project_memory",
    "task_state",
    "observability",
    "failure_attribution",
    "verification",
    "permissions",
    "entropy_auditing",
    "intervention_recording",
    "coordination",
}


def validate_manifest(path: Path) -> List[str]:
    errors: List[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]

    missing = sorted(REQUIRED_TOP_LEVEL - data.keys())
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(missing)}")

    task_id = data.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        errors.append(f"{path}: task_id must be a non-empty string")

    gap = data.get("harness_gap", {})
    gap_class = gap.get("class") if isinstance(gap, dict) else None
    if gap_class not in VALID_CLASSES:
        errors.append(f"{path}: invalid harness_gap.class: {gap_class!r}")

    components = data.get("harness_components")
    if not isinstance(components, list) or not components:
        errors.append(f"{path}: harness_components must be a non-empty list")
    else:
        invalid = sorted(set(components) - VALID_COMPONENTS)
        if invalid:
            errors.append(f"{path}: invalid harness_components: {', '.join(invalid)}")

    observability = data.get("observability", {})
    if not isinstance(observability, dict):
        errors.append(f"{path}: observability must be an object")
    else:
        for field in ("component_signals", "trajectory_signals", "decision_signals"):
            value = observability.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"{path}: observability.{field} must be a non-empty list")

    contract = data.get("decision_contract", {})
    if not isinstance(contract, dict):
        errors.append(f"{path}: decision_contract must be an object")
    else:
        for field in ("hypothesis", "expected_effect", "falsification_check"):
            value = contract.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"{path}: decision_contract.{field} must be a string")

    safety = data.get("safety_constraints", {})
    if not isinstance(safety, dict):
        errors.append(f"{path}: safety_constraints must be an object")
    else:
        for field in ("permissions", "information_boundaries"):
            value = safety.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"{path}: safety_constraints.{field} must be a non-empty list")

    for field in ("allowed_harness_edits", "visible_checks", "hidden_checks"):
        value = data.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"{path}: {field} must be a non-empty list")

    replay = data.get("replay_protocol", {})
    if not isinstance(replay, dict):
        errors.append(f"{path}: replay_protocol must be an object")
    else:
        for field in ("checkpoint", "reset", "replay", "success_criteria"):
            if field not in replay:
                errors.append(f"{path}: replay_protocol missing {field}")

    episode = data.get("episode_package", {})
    if not isinstance(episode, dict):
        errors.append(f"{path}: episode_package must be an object")
    elif not isinstance(episode.get("required_artifacts"), list) or not episode.get(
        "required_artifacts"
    ):
        errors.append(f"{path}: episode_package.required_artifacts must be a non-empty list")

    return errors


def validate_manifests(root: Path) -> Tuple[List[str], int]:
    paths = sorted(root.rglob("*.json"))
    if not paths:
        return [f"No manifests found under {root}"], 0

    all_errors: List[str] = []
    for path in paths:
        all_errors.extend(validate_manifest(path))
    return all_errors, len(paths)
