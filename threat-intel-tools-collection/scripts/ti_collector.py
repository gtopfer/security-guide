"""Utilities to normalize threat intelligence inputs and generate quick reports."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, MutableMapping

DEFAULT_CONFIDENCE = "medio"


def _normalize_entry(entry: MutableMapping[str, object]) -> MutableMapping[str, object]:
    """Return a normalized IOC/alert entry with mandatory fields."""
    normalized = {
        "type": str(entry.get("type") or entry.get("category") or "unknown").lower(),
        "value": str(entry.get("value") or entry.get("indicator") or "").strip(),
        "confidence": str(entry.get("confidence") or DEFAULT_CONFIDENCE).lower(),
        "source": entry.get("source") or entry.get("feed") or "desconhecido",
        "tags": entry.get("tags") or entry.get("ttp") or [],
        "first_seen": entry.get("first_seen") or entry.get("timestamp"),
        "last_seen": entry.get("last_seen"),
    }
    if not normalized["value"]:
        raise ValueError("Cada IOC/alerta precisa conter o campo 'value'.")
    return normalized


def compile_ioc_report(
    entries: Iterable[MutableMapping[str, object]],
    output_path: Path | str,
    *,
    detection_type: str = "ioc",
) -> Path:
    """Normalize entries, drop duplicates and persist a JSON report."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    normalized_items: List[MutableMapping[str, object]] = []
    dedup_key = set()
    for raw in entries:
        normalized = _normalize_entry(raw)
        key = (normalized["type"], normalized["value"])
        if key in dedup_key:
            continue
        dedup_key.add(key)
        normalized_items.append(normalized)

    by_type = Counter(item["type"] for item in normalized_items)
    by_confidence = Counter(item["confidence"] for item in normalized_items)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "detection_type": detection_type,
        "total": len(normalized_items),
        "by_type": dict(by_type),
        "by_confidence": dict(by_confidence),
        "items": normalized_items,
    }

    output.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    return output


def _load_entries_from_file(path: Path) -> List[MutableMapping[str, object]]:
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError("O arquivo precisa conter uma lista de objetos.")
    return [dict(item) for item in data]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize IOCs/alertas e gere relatório JSON.")
    parser.add_argument("--ioc-file", required=True, help="Arquivo JSON com lista de indicadores/alertas.")
    parser.add_argument("--out", required=True, help="Destino do relatório normalizado.")
    parser.add_argument(
        "--detection-type",
        default="ioc",
        help="Rótulo para o tipo de dado (ex.: ioc, alert, hunting).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    source = Path(args.ioc_file)
    entries = _load_entries_from_file(source)
    compile_ioc_report(entries, Path(args.out), detection_type=args.detection_type)


if __name__ == "__main__":
    main()
