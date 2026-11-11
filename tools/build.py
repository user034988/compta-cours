#!/usr/bin/env python3
"""Assemble index.html (site GitHub Pages) à partir de src/app.html.

src/app.html est la page elle-même, sans <html>/<head>/<body> : c'est aussi la version
publiée comme artifact Claude. Ce script l'entoure d'un document complet et ajoute
la connexion Supabase (config publique + bibliothèque supabase-js).

Usage : python3 tools/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "app.html"
OUT = ROOT / "index.html"

# Clé publiable : elle est faite pour être visible dans le navigateur.
# Les données restent protégées par les règles RLS de la table « documents ».
SUPABASE_URL = "https://efnxedcbkgnphjrnlnvd.supabase.co"
SUPABASE_KEY = "sb_publishable_3X3l8OgQosV4QQNXPORQIg_qMvCrxMh"
SUPABASE_JS = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.58.0/dist/umd/supabase.js"

ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3E"
        "%3Crect x='1' y='1' width='28' height='28' rx='6' fill='%232D4A73'/%3E"
        "%3Cpath d='M8 10h14M8 15h14M8 20h14' stroke='white' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E")

RESET = (":root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
         "body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}")


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    marker = '<div class="app" id="app">'
    head_part, body_part = src.split(marker, 1)
    body_part = marker + body_part
    head_part = head_part.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    first_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/'
    assert body_part.count(first_script) == 1, "point d'insertion des scripts introuvable"
    config = (
        f'<script>window.COMPTA_CONFIG = {{ url: "{SUPABASE_URL}", key: "{SUPABASE_KEY}" }};</script>\n'
        f'<script src="{SUPABASE_JS}"></script>\n'
    )
    body_part = body_part.replace(first_script, config + first_script)
    html = (
        "<!doctype html>\n<html lang=\"fr\">\n<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="Saisie d\'écritures comptables au bordereau et tableaux d\'amortissement fiscal, économique et dérogatoire.">\n'
        f'<link rel="icon" href="{ICON}">\n'
        f"<style>{RESET}</style>\n"
        + head_part.strip() + "\n</head>\n<body>\n" + body_part.strip() + "\n</body>\n</html>\n"
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} : {len(html):,} caractères")


if __name__ == "__main__":
    main()
