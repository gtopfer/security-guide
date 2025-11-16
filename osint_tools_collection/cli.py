from __future__ import annotations

from pathlib import Path
import runpy
import sys


def main() -> None:
    """Executa o script `scripts/osint_collector.py` no contexto atual.

    O wrapper permite instalação via `pip install -e .` e expõe um entry-point
    que será instalado como comando `osint-collector`.
    """
    base = Path(__file__).parent
    script = base.parent / "scripts" / "osint_collector.py"
    if not script.exists():
        print(f"[!] script not found: {script}", file=sys.stderr)
        raise SystemExit(2)
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
