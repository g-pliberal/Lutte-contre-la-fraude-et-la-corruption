#!/usr/bin/env python3
"""Écrit les sept pages du site à la racine du dépôt.

    python3 scripts/construire.py

Le site servi est du HTML statique, versionné&nbsp;: il n'y a rien à exécuter
pour le lire, et aucun serveur à faire tourner. Ce script n'existe que pour que
le bandeau, le pied et l'affiche n'aient qu'un seul point de vérité — un onglet
ajouté à la main sur six pages sur sept est un onglet manquant.

Il est donc à relancer après toute modification de ``gabarit.py`` ou de
``pages.py``, et les fichiers qu'il produit sont commités avec la source.
"""

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import pages  # noqa: E402  (le chemin doit être posé d'abord)

#: Le fichier produit, et la fonction qui l'écrit. L'ordre est celui de la
#: navigation : il se relit comme le plan du site.
SITE = (
    ("index.html", pages.accueil),
    ("constat.html", pages.constat),
    ("dispositif.html", pages.dispositif),
    ("diagnostic.html", pages.diagnostic),
    ("programme.html", pages.programme),
    ("chiffrage.html", pages.chiffrage),
    ("sources.html", pages.sources),
)


def main() -> int:
    for fichier, rendre in SITE:
        chemin = RACINE / fichier
        chemin.write_text(rendre(), encoding="utf-8")
        print(f"{fichier:20s} {chemin.stat().st_size:>7d} octets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
