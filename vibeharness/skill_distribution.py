"""Validation for the distributable VibeHarness skill."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path
from typing import List, Optional, Tuple


DISALLOWED_SKILL_DOCS = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}


def _has_frontmatter_field(text: str, field: str, expected_prefix: Optional[str] = None) -> bool:
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    frontmatter = text[4:end].splitlines()
    prefix = f"{field}:"
    for line in frontmatter:
        if not line.startswith(prefix):
            continue
        value = line[len(prefix) :].strip()
        if expected_prefix is None:
            return bool(value)
        return value.startswith(expected_prefix)
    return False


def check_skill_distribution(root: Path) -> Tuple[List[str], int]:
    """Return validation errors and number of distribution checks performed."""

    errors: List[str] = []
    checks = 0
    skill_dir = root / "skills" / "vibeharness"
    repo_skill_dir = root / ".agents" / "skills" / "vibeharness"
    skill_md = skill_dir / "SKILL.md"
    repo_skill_md = repo_skill_dir / "SKILL.md"
    root_skill_md = root / "SKILL.md"
    reference = skill_dir / "references" / "episode-format.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    installer = root / "install.sh"

    for required in [skill_md, repo_skill_md, root_skill_md, reference, openai_yaml, installer]:
        checks += 1
        if not required.exists():
            errors.append(f"{required.relative_to(root)}: missing")

    if skill_md.exists():
        checks += 2
        text = skill_md.read_text(encoding="utf-8")
        if not _has_frontmatter_field(text, "name", "vibeharness"):
            errors.append("skills/vibeharness/SKILL.md: missing name frontmatter")
        if not _has_frontmatter_field(text, "description"):
            errors.append("skills/vibeharness/SKILL.md: missing description frontmatter")

    if root_skill_md.exists() and skill_md.exists():
        checks += 1
        if root_skill_md.read_text(encoding="utf-8") != skill_md.read_text(encoding="utf-8"):
            errors.append("SKILL.md and skills/vibeharness/SKILL.md are out of sync")

    if repo_skill_dir.exists() and skill_dir.exists():
        checks += 1
        completed = subprocess.run(
            ["diff", "-qr", str(skill_dir), str(repo_skill_dir)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if completed.returncode != 0:
            errors.append(".agents/skills/vibeharness and skills/vibeharness are out of sync")

    if skill_dir.exists():
        for name in sorted(DISALLOWED_SKILL_DOCS):
            checks += 1
            if (skill_dir / name).exists():
                errors.append(f"skills/vibeharness/{name}: keep auxiliary docs outside skill folder")

    if installer.exists():
        checks += 1
        if not os.access(installer, os.X_OK):
            errors.append("install.sh: not executable")

    if installer.exists() and skill_md.exists():
        checks += 3
        with tempfile.TemporaryDirectory(prefix="vh-skill-install-") as tmp:
            tmp_path = Path(tmp)
            env = os.environ.copy()
            env["HOME"] = str(tmp_path / "home")
            env["AGENTS_HOME"] = str(tmp_path / "agents")
            env["CODEX_HOME"] = str(tmp_path / "codex")
            completed = subprocess.run(
                ["bash", str(installer), "--force"],
                cwd=root,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if completed.returncode != 0:
                errors.append(
                    "install.sh smoke test failed: "
                    + (completed.stderr.strip() or completed.stdout.strip())
                )
            codex_standard_skill = tmp_path / "agents" / "skills" / "vibeharness" / "SKILL.md"
            codex_compat_skill = tmp_path / "codex" / "skills" / "vibeharness" / "SKILL.md"
            claude_skill = tmp_path / "home" / ".claude" / "skills" / "vibeharness" / "SKILL.md"
            if not codex_standard_skill.exists():
                errors.append("install.sh smoke test did not install Codex standard skill")
            if not codex_compat_skill.exists():
                errors.append("install.sh smoke test did not install Codex compatibility skill")
            if not claude_skill.exists():
                errors.append("install.sh smoke test did not install Claude skill")

    return errors, checks
