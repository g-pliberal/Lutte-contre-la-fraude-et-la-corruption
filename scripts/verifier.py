#!/usr/bin/env python3
"""Les vérifications qui tiennent le site debout.

    python3 scripts/verifier.py

Un site statique de sept pages n'a pas besoin d'une suite de tests, mais il a
besoin de ces cinq-là : ce sont exactement les erreurs qu'on ne voit pas en
relisant, et qu'un lecteur voit tout de suite.

  1. le balisage est équilibré ;
  2. tout lien interne mène quelque part — fichier et ancre ;
  3. chaque page a son onglet actif, et un seul ;
  4. toute classe écrite dans le HTML existe dans la feuille de style
     (une faute de frappe dans un nom de classe est un bloc sans style, et
     rien ne le signale) ;
  5. les fichiers que l'en-tête appelle existent, chaque page porte un titre
     de premier niveau — un seul —, et aucune entité HTML n'a été échappée
     deux fois.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAGES = sorted(RACINE.glob("*.html"))

#: Les éléments qui n'ont pas de fermeture : les compter comme ouverts ferait
#: échouer la vérification d'équilibre sur chaque <meta>.
ORPHELINS = {"meta", "link", "img", "br", "hr", "input", "source", "col",
             "area", "base", "embed", "param", "track", "wbr"}


class Arbre(HTMLParser):
    """Compte les ouvertures et les fermetures, et relève les identifiants,
    les classes, les liens et les ancres."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pile: list[str] = []
        self.fautes: list[str] = []
        self.identifiants: set[str] = set()
        self.classes: set[str] = set()
        self.liens: list[str] = []
        self.actifs = 0

    def handle_starttag(self, balise: str, attributs: list) -> None:
        table = dict(attributs)
        if identifiant := table.get("id"):
            self.identifiants.add(identifiant)
        self.classes.update((table.get("class") or "").split())
        if table.get("href"):
            self.liens.append(table["href"])
        if table.get("aria-current") == "page":
            self.actifs += 1
        if balise not in ORPHELINS:
            self.pile.append(balise)

    def handle_endtag(self, balise: str) -> None:
        if balise in ORPHELINS:
            return
        if not self.pile:
            self.fautes.append(f"</{balise}> sans ouverture")
        elif self.pile[-1] != balise:
            self.fautes.append(f"</{balise}> ferme <{self.pile[-1]}>")
            if balise in self.pile:
                while self.pile.pop() != balise:
                    pass
        else:
            self.pile.pop()


def classes_de_la_feuille() -> set[str]:
    """Les noms de classe que la feuille de style connaît."""
    feuille = (RACINE / "ressources" / "style.css").read_text(encoding="utf-8")
    # Les commentaires portent des noms de classe en prose (« voir `.defilant` »)
    # qui ne sont pas des sélecteurs : les retirer d'abord.
    feuille = re.sub(r"/\*.*?\*/", " ", feuille, flags=re.S)
    return set(re.findall(r"\.([a-zA-Z_][\w-]*)", feuille))


def main() -> int:
    fautes: list[str] = []
    noms = {chemin.name for chemin in PAGES}
    connues = classes_de_la_feuille()

    # Les identifiants de TOUTES les pages sont relevés d'abord : sans cela,
    # une ancre pointant vers une autre page — « sources.html#fiscal » — ne
    # pourrait pas être vérifiée, et c'est précisément celle qui se casse
    # quand on renomme une section.
    arbres = {}
    for chemin in PAGES:
        arbre = Arbre()
        arbre.feed(chemin.read_text(encoding="utf-8"))
        arbre.close()
        arbres[chemin.name] = arbre

    for chemin in PAGES:
        arbre = arbres[chemin.name]
        texte = chemin.read_text(encoding="utf-8")
        prefixe = chemin.name

        for faute in arbre.fautes:
            fautes.append(f"{prefixe}: balisage — {faute}")
        if arbre.pile:
            fautes.append(f"{prefixe}: balises jamais fermées — {arbre.pile}")

        # Une entité doublement échappée — « &amp;nbsp; » — s'écrit en
        # toutes lettres dans la page : c'est le signe qu'une entité HTML a
        # été passée à une fonction qui attend du texte.
        for entite in set(re.findall(r"&amp;[a-zA-Z]+;", texte)):
            fautes.append(f"{prefixe}: entité doublement échappée « {entite} »")

        titres = len(re.findall(r"<h1\b", texte))
        if titres != 1:
            fautes.append(f"{prefixe}: {titres} <h1>, il en faut exactement un")

        if arbre.actifs != 1:
            fautes.append(f"{prefixe}: {arbre.actifs} onglet(s) actif(s), "
                          "il en faut exactement un")

        for lien in arbre.liens:
            if lien.startswith(("http://", "https://", "mailto:")):
                continue
            cible, _, ancre = lien.partition("#")
            if cible and cible not in noms and not (RACINE / cible).exists():
                fautes.append(f"{prefixe}: lien mort vers « {cible} »")
            if not ancre or ancre == "contenu":
                continue
            ailleurs = arbres[cible].identifiants if cible in arbres \
                else arbre.identifiants
            if ancre not in ailleurs:
                fautes.append(f"{prefixe}: ancre « {lien} » introuvable")

        for classe in sorted(arbre.classes - connues):
            fautes.append(f"{prefixe}: classe « {classe} » absente de la feuille")

    for exigé in ("ressources/style.css", "ressources/icone.svg",
                  "ressources/polices/public-sans-latin.woff2",
                  "ressources/polices/instrument-serif-latin.woff2"):
        if not (RACINE / exigé).exists():
            fautes.append(f"fichier manquant : {exigé}")

    for faute in fautes:
        print(faute, file=sys.stderr)
    print(f"{len(PAGES)} pages vérifiées, {len(fautes)} faute(s).")
    return 1 if fautes else 0


if __name__ == "__main__":
    raise SystemExit(main())
