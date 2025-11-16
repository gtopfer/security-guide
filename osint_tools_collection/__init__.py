"""Pacote wrapper para expor CLI da coleção OSINT.

Este pacote fornece um ponto de entrada leve (`osint-collector`) que executa
o script `scripts/osint_collector.py` presente na coleção. Útil para
instalação via `pip install -e .` a partir da pasta `Security-Guide`.
"""
__all__ = ["cli"]

__version__ = "0.1.0"
