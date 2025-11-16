#!/usr/bin/env bash
# Consulta certificados do CRT.sh e retorna CNs/subdomínios únicos.
set -euo pipefail
if [ $# -eq 0 ] && [ -z "${CRTSH_DOMAIN:-}" ]; then
  echo "Uso: CRTSH_DOMAIN=exemplo.com ./crtsh.sh" >&2
  exit 1
fi
DOMAIN=${1:-$CRTSH_DOMAIN}
QUERY="https://crt.sh/?q=%25.${DOMAIN}&output=json"
curl -s "$QUERY" \
  | jq -r '.[].name_value' \
  | tr '[:upper:]' '[:lower:]' \
  | sort -u
