#!/usr/bin/env python3
"""Les vérifications qui tiennent le site debout.

    python3 scripts/verifier.py

Un site statique de huit pages n'a pas besoin d'une suite de tests, mais il a
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

Une sixième vérification existe, et elle ne tourne QUE sur demande :

    python3 scripts/verifier.py --liens

Elle interroge une à une les adresses extérieures citées par le site. Ce site
promet que tout y est vérifiable ; une source dont l'adresse a disparu casse
cette promesse en silence, et rien d'autre ne le signale. Elle n'est pas dans
le contrôle par défaut parce qu'elle a besoin du réseau.

Elle trie ses résultats en TROIS catégories, et c'est tout l'intérêt : sur
trente et une adresses, la moitié des administrations françaises et
américaines citées ici refusent de répondre à autre chose qu'un navigateur.
Un outil qui les compterait comme des fautes serait ignoré au bout de deux
exécutions, et le lien réellement mort passerait avec elles.

  - « lien mort » : le serveur répond et dit que la page n'existe pas
    (404, 410). C'est une faute du dépôt, et la seule qui fasse échouer
    la commande.
  - « refus » : le serveur est vivant et refuse un outil automatique
    (403, 405, 429). La page existe probablement ; à vérifier à la main.
  - « indéterminé » : la connexion n'aboutit pas (coupure, échec TLS, DNS).
    Cela ne dit rien de la page.

À relancer avant chaque revue des chiffres.
"""

import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

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


#: Certains hébergeurs refusent une requête sans navigateur déclaré, et
#: répondent 403 à un outil qui se présente comme tel. On se nomme, et on
#: attend : un contrôle de liens qui ment sur ce qu'il est vérifie mal.
AGENT = ("Mozilla/5.0 (compatible; verificateur-de-liens/1.0; "
         "+https://github.com/g-pliberal/Lutte-contre-la-fraude-et-la-corruption)")

DELAI = 20


def adresses_externes() -> dict[str, set[str]]:
    """Les adresses extérieures citées, et les pages qui les citent."""
    trouvees: dict[str, set[str]] = {}
    for chemin in PAGES:
        arbre = Arbre()
        arbre.feed(chemin.read_text(encoding="utf-8"))
        arbre.close()
        for lien in arbre.liens:
            if lien.startswith(("http://", "https://")):
                trouvees.setdefault(lien, set()).add(chemin.name)
    return trouvees


#: Les codes par lesquels un serveur bien vivant écarte un outil automatique.
#: Ils ne disent rien de l'existence de la page — seulement de qui la demande.
REFUS = {401, 403, 405, 406, 429, 999}

#: Les codes par lesquels un serveur affirme que la page n'existe pas. Eux
#: seuls sont des fautes du dépôt.
MORT = {404, 410}


def interroger(adresse: str) -> tuple:
    """Rend ``(categorie, motif)`` : ``""`` si l'adresse répond, sinon
    ``"mort"``, ``"refus"`` ou ``"indetermine"``.

    On essaie ``HEAD`` d'abord — c'est la requête polie, elle ne rapatrie pas
    la page —, puis ``GET`` si le serveur ne la comprend pas : beaucoup
    répondent 405 à ``HEAD`` alors que la page existe.
    """
    categorie, motif = "indetermine", "aucune réponse"
    for methode in ("HEAD", "GET"):
        requete = urllib.request.Request(
            adresse, method=methode, headers={"User-Agent": AGENT})
        try:
            with urllib.request.urlopen(requete, timeout=DELAI) as reponse:
                if reponse.status < 400:
                    return "", ""
                code = reponse.status
            categorie = ("mort" if code in MORT
                         else "refus" if code in REFUS else "indetermine")
            motif = f"code {code}"
        except urllib.error.HTTPError as erreur:
            if erreur.code in REFUS and methode == "HEAD":
                continue          # le serveur écarte HEAD : réessayer en GET
            categorie = ("mort" if erreur.code in MORT
                         else "refus" if erreur.code in REFUS
                         else "indetermine")
            motif = f"code {erreur.code}"
        except urllib.error.URLError as erreur:
            categorie, motif = "indetermine", f"injoignable ({erreur.reason})"
        except Exception as erreur:  # noqa: BLE001 — on rapporte, on n'arrête pas
            categorie = "indetermine"
            motif = f"{type(erreur).__name__}: {erreur}"
        if methode == "GET":
            break
    return categorie, motif


#: L'intitulé de chaque catégorie, et l'ordre dans lequel on les imprime :
#: ce qui est une faute d'abord, ce qui n'en est pas ensuite.
CATEGORIES = (
    ("mort", "LIENS MORTS — le serveur dit que la page n'existe pas"),
    ("refus", "REFUS — serveur vivant qui écarte un outil automatique ; "
              "à vérifier dans un navigateur"),
    ("indetermine", "INDÉTERMINÉ — la connexion n'a pas abouti ; ne dit rien "
                    "de la page"),
)


def verifier_les_liens() -> int:
    """Le contrôle des adresses extérieures. Rend le nombre de liens MORTS.

    Les refus et les indéterminés sont imprimés mais ne font pas échouer la
    commande : les compter comme des fautes reviendrait à la rendre toujours
    rouge, donc à ne plus la lire.
    """
    trouvees = adresses_externes()
    releve: dict[str, list] = {nom: [] for nom, _ in CATEGORIES}
    for adresse in sorted(trouvees):
        categorie, motif = interroger(adresse)
        if categorie:
            releve[categorie].append((adresse, motif))

    for nom, intitule in CATEGORIES:
        if not releve[nom]:
            continue
        print(f"\n{intitule}", file=sys.stderr)
        for adresse, motif in releve[nom]:
            pages = ", ".join(sorted(trouvees[adresse]))
            print(f"  {urlsplit(adresse).netloc} — {motif}\n"
                  f"    {adresse}\n    cité par {pages}", file=sys.stderr)

    morts = len(releve["mort"])
    valides = len(trouvees) - sum(len(v) for v in releve.values())
    print(f"\n{len(trouvees)} adresses interrogées : {valides} valides, "
          f"{morts} morte(s), {len(releve['refus'])} refus, "
          f"{len(releve['indetermine'])} indéterminée(s).")
    if not morts:
        print("Aucun lien mort.")
    return morts


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
    if "--liens" in sys.argv[1:]:
        raise SystemExit(1 if verifier_les_liens() else 0)
    raise SystemExit(main())
