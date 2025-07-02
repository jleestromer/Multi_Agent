"""Utility helpers for the multi-agent framework."""

from pathlib import Path


def write_file(path: str, content: str) -> None:
    """Write content to disk creating parent directories if needed."""

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
