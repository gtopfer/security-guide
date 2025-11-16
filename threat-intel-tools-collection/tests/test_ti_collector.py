from pathlib import Path
import json

from scripts.ti_collector import compile_ioc_report


def test_compile_ioc_report_deduplicates(tmp_path: Path) -> None:
    sample_entries = [
        {"type": "domain", "value": "malicious.example", "confidence": "alto"},
        {"type": "domain", "value": "malicious.example", "confidence": "medio"},
        {"type": "ip", "value": "203.0.113.42", "confidence": "baixo"},
    ]
    out_path = tmp_path / "report.json"
    compile_ioc_report(sample_entries, out_path, detection_type="ioc")

    data = json.loads(out_path.read_text())
    assert data["total"] == 2
    assert data["by_type"]["domain"] == 1
    assert data["by_confidence"]["alto"] == 1
    values = {item["value"] for item in data["items"]}
    assert "malicious.example" in values
    assert "203.0.113.42" in values
