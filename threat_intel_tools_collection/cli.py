from __future__ import annotations

from pathlib import Path
import runpy
import sys


def main() -> None:
    base = Path(__file__).parent
    script = base.parent / "scripts" / "ti_collector.py"
    if not script.exists():
        print(f"[!] script not found: {script}", file=sys.stderr)
        raise SystemExit(2)
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
