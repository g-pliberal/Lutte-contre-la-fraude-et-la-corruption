"""Le gabarit du site : ce qui est le même sur toutes les pages.

Les huit pages sont du HTML statique, écrit une fois et servi tel quel. Mais le
bandeau, le pied et l'affiche ne doivent exister qu'à UN seul endroit : un
onglet ajouté à la main sur sept pages sur huit est un onglet manquant, et cela
finit toujours par arriver. Ce module les écrit, ``construire.py`` les assemble,
et les fichiers produits sont versionnés — le site se sert sans rien exécuter.

La charte est celle de « Retraite à comptes notionnels » : même vert profond,
même or, mêmes deux polices, mêmes noms de variables CSS. Les deux sites sont
des outils du même parti, et un électeur qui passe de l'un à l'autre doit
reconnaître la maison.
"""

from html import escape

#: L'adresse du dépôt, citée dans le pied : ce qui est écrit ici est
#: vérifiable, et l'endroit où le vérifier doit tenir sur une ligne.
DEPOT = "https://github.com/g-pliberal/Lutte-contre-la-fraude-et-la-corruption"
SITE_PARENT = "https://partiliberalfrancais.fr/"
NOM_SITE = "Lutte contre la fraude et la corruption"

#: Le mois de la dernière revue des chiffres. Il est écrit une fois et repris
#: par le pied de chaque page : un site qui cite des ordres de grandeur doit
#: dire quand il les a regardés pour la dernière fois.
REVUE = "septembre 2026"

#: Les onglets, par groupe. Les étiquettes de groupe sont du TEXTE, lu par les
#: synthèses vocales — c'est le style qui les sort de l'écran, pas ce fichier,
#: et la classification reste donc vraie pour qui l'entend.
GROUPES_NAVIGATION = (
    ("Le projet", (("index.html", "Le projet"),)),
    ("Ce qui est", (("constat.html", "Constat"),
                    ("dispositif.html", "Dispositif"),
                    ("diagnostic.html", "Diagnostic"))),
    ("Ce que nous proposons", (("programme.html", "Programme"),
                               ("chiffrage.html", "Chiffrage"),
                               ("objections.html", "Objections"))),
    ("La confiance", (("sources.html", "Sources"),)),
)

#: Les pictogrammes du site, et rien qu'eux. Ils viennent tous de Lucide, sous
#: licence ISC : une seule grille — 24 × 24, trait de 2, extrémités arrondies —,
#: si bien qu'ils tiennent ensemble à toutes les tailles. Le tracé est écrit
#: ICI et non chargé : la page ne demande aucune ressource à un tiers.
ICONES = {
    "chevron-down": '<path d="m6 9 6 6 6-6" />',
    "shield-check": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 '
                    '20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 '
                    '1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z" />'
                    '<path d="m9 12 2 2 4-4" />',
    "triangle-alert":
        '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 '
        '0 0 0 1.73-3" /><path d="M12 9v4" /><path d="M12 17h.01" />',
}

ENVELOPPE_ICONE = (
    'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round"'
)


def icone(nom: str, titre: str = "") -> str:
    """Un pictogramme, écrit dans la page.

    Sans ``titre`` il est DÉCORATIF : le texte à côté dit déjà ce qu'il dit, et
    le répéter ferait entendre deux fois la même chose à une synthèse vocale.
    Avec ``titre``, il porte à lui seul une information et devient une image
    nommée.
    """
    if titre:
        role = f'role="img" aria-label="{escape(titre)}"'
    else:
        role = 'aria-hidden="true" focusable="false"'
    return (f'<svg class="icone" {ENVELOPPE_ICONE} {role}>'
            f'{ICONES[nom]}</svg>')


def navigation(page_active: str) -> str:
    """Les onglets du bandeau, par groupe."""
    def liens(groupe: tuple) -> str:
        return "".join(
            f'<a href="{fichier}"'
            + (' aria-current="page"' if fichier == page_active else "")
            + f">{escape(libelle)}</a>"
            for fichier, libelle in groupe
        )
    return "".join(
        f'<span class="groupe"><span class="etiquette">{escape(etiquette)}</span>'
        f'<span class="liens">{liens(groupe)}</span></span>'
        for etiquette, groupe in GROUPES_NAVIGATION
    )


def entete(page_active: str) -> str:
    """Bandeau de tête, précédé du lien d'évitement.

    Le lien d'évitement est le premier élément parcouru au clavier : sans lui,
    atteindre le contenu depuis la barre d'adresse impose de traverser les huit
    onglets à chaque page (WCAG 2.4.1).

    Le nom du site n'est PAS un ``<h1>`` : chaque page porte son propre titre,
    énorme et en capitales, et c'est lui le ``<h1>``. « Lutte contre la fraude
    et la corruption » est le nom du site, répété à l'identique huit fois.
    """
    return f"""<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="bandeau"><div class="interieur">
  <p class="nom"><a href="index.html"><span>{escape(NOM_SITE)}</span></a></p>
  <nav aria-label="Navigation principale">{navigation(page_active)}</nav>
</div></header>"""


def affiche(surtitre: str, titre: str, chapeau: str) -> str:
    """Le bloc de tête d'une page : sur-titre, titre massif, chapeau.

    ``titre`` et ``chapeau`` sont du HTML — ils portent les passages en or et
    les liens. ``surtitre`` est du texte. Le titre est mis en capitales PAR LE
    STYLE, jamais dans le texte : certaines synthèses vocales épellent lettre à
    lettre un mot écrit en majuscules.
    """
    return (f'<div class="affiche"><p class="surtitre">{escape(surtitre)}</p>'
            f'<h1>{titre}</h1><p class="chapeau">{chapeau}</p></div>')


def plan(entrees: tuple) -> str:
    """Le plan d'une page longue : ce qu'elle contient, avant de la lire."""
    liens = "".join(f'<li><a href="#{ancre}">{escape(libelle)}</a></li>'
                    for ancre, libelle in entrees)
    return ('<nav class="plan" aria-label="Dans cette page">'
            '<p class="etiquette">Dans cette page</p>'
            f'<ol>{liens}</ol></nav>')


def reperes(fiches: tuple) -> str:
    """La frise de chiffres d'ouverture d'une page.

    L'étiquette passe AU-DESSUS du nombre : on lit « ce qui échappe » puis
    « 6 à 100 Md € », dans cet ordre, et non un nombre dont on cherche le sens.
    ``precision`` est du HTML, et porte la source.
    """
    blocs = "".join(
        f'<div class="fiche"><div class="etiquette">{escape(etiquette)}</div>'
        f'<div class="valeur">{escape(valeur)}</div>'
        f'<div class="precision">{precision}</div></div>'
        for etiquette, valeur, precision in fiches
    )
    return f'<div class="fiches reperes">{blocs}</div>'


def engagements(liste: tuple) -> str:
    """Les quatre chiffres du programme, numérotés 01 à 04.

    La numérotation les fait lire comme une liste d'engagements et non comme
    quatre statistiques orphelines. ``promesse`` et ``detail`` sont du HTML.
    """
    cartes = "".join(
        f'<div class="engagement"><p class="rang">{rang:02d}</p>'
        f'<p class="chiffre">{escape(chiffre)}</p>'
        f'<p class="promesse">{promesse}</p>'
        f'<p class="detail">{detail}</p></div>'
        for rang, (chiffre, promesse, detail) in enumerate(liste, start=1)
    )
    return ('<section class="engagements" aria-label="Nos quatre engagements">'
            f'<div class="grille">{cartes}</div></section>')


def gestes(liste: tuple) -> str:
    """La méthode, en trois lignes numérotées. Chaque entrée est du HTML."""
    lignes = "".join(f'<li><span class="rang">{rang}</span><span>{texte}</span></li>'
                     for rang, texte in enumerate(liste, start=1))
    return f'<ol class="gestes">{lignes}</ol>'


def points(liste: tuple) -> str:
    """Quelques idées, une par bloc, de même poids.

    C'est ce qui les distingue d'une liste, où la première l'emporte.
    """
    blocs = "".join(f'<div class="point"><h3>{escape(titre)}</h3><p>{texte}</p></div>'
                    for titre, texte in liste)
    return f'<div class="points">{blocs}</div>'


def cle(question: str, reponse: str, corps: str, source: str = "",
        identifiant: str = "") -> str:
    """Une question, sa réponse en une phrase, et ce qui la montre.

    Elle est faite pour deux lecteurs à la fois : celui qui n'a pas le temps
    lit la question et la réponse et s'arrête là ; celui qui veut voir descend
    d'un cran et trouve le tableau, puis sa source. Elle est encadrée pour une
    troisième raison : elle doit se découper. Une capture de ce bloc porte la
    question, la réponse et la source — elle se comprend hors du site.
    """
    fin = f'<p class="source">{source}</p>' if source else ""
    cible = f' id="{escape(identifiant)}" tabindex="-1"' if identifiant else ""
    return (f'<section class="cle"{cible}><h3>{escape(question)}</h3>'
            f'<p class="reponse">{reponse}</p>{corps}{fin}</section>')


def mesures(liste: tuple, depart: int = 1) -> str:
    """Les mesures du programme : rang, titre, effet, et ce qu'elles remplacent.

    La ligne « Aujourd'hui » n'est pas un ornement : sans elle, une mesure ne
    se lit pas comme une alternative mais comme un vœu.

    ``depart`` donne le rang de la première mesure du bloc, et il est
    obligatoire dès le deuxième : le programme est découpé en trois blocs mais
    sa numérotation est CONTINUE, et le reste du site y renvoie par le numéro
    — « la mesure n° 8 ». Trois blocs qui repartiraient de 01 afficheraient
    trois fois le même rang, et aucun renvoi ne désignerait plus rien.
    ``start`` de ``enumerate`` porte donc le décalage, et ``__doc__`` le dit
    pour que personne n'ajoute un bloc en l'oubliant.
    """
    lignes = "".join(
        f'<li value="{rang}"><span class="rang">{rang:02d}</span><div class="corps">'
        f'<h3>{escape(titre)}</h3>{corps}'
        f'<p class="aujourdhui"><b>Aujourd\'hui —</b> {actuel}</p>'
        f'</div></li>'
        for rang, (titre, corps, actuel) in enumerate(liste, start=depart)
    )
    return f'<ol class="mesures" start="{depart}">{lignes}</ol>'


def tableau(legende: str, entetes: tuple, lignes: tuple,
            classes: tuple = ()) -> str:
    """Un tableau, dans un cadre qui défile s'il est plus large que l'écran.

    Le cadre porte ``tabindex="0"`` : une boîte défilante qui ne peut pas
    recevoir le focus est inatteignable au clavier chez plusieurs moteurs
    (WCAG 2.1.1). La légende est énoncée par les synthèses vocales avant le
    contenu, et son ``<span>`` collant la garde visible pendant le défilement.

    ``classes`` donne, colonne par colonne, ``texte``, ``nombre`` ou ``long``.
    Les cellules sont du HTML : elles portent des liens et des mises en
    évidence.
    """
    def classe(rang: int) -> str:
        nom = classes[rang] if rang < len(classes) else ""
        return f' class="{nom}"' if nom else ""

    tete = "".join(f'<th scope="col"{classe(rang)}>{escape(libelle)}</th>'
                   for rang, libelle in enumerate(entetes))
    corps = "".join(
        "<tr>" + "".join(
            (f'<th scope="row"{classe(rang)}>{cellule}</th>' if rang == 0
             else f'<td{classe(rang)}>{cellule}</td>')
            for rang, cellule in enumerate(ligne)
        ) + "</tr>"
        for ligne in lignes
    )
    return (f'<div class="defilant" tabindex="0" role="region" '
            f'aria-label="{escape(legende)}">'
            f'<table><caption><span>{escape(legende)}</span></caption>'
            f'<thead><tr>{tete}</tr></thead><tbody>{corps}</tbody></table></div>')


def depliant(titre: str, corps: str) -> str:
    """Une section repliée. Son titre a le poids d'un intertitre, parce qu'il
    en tient lieu : c'est lui qu'on parcourt pour savoir ce que la page
    contient encore.
    """
    return (f'<details class="section"><summary>{icone("chevron-down")}'
            f'<span>{escape(titre)}</span></summary>'
            f'<div class="dedans">{corps}</div></details>')


def vigilance(texte: str) -> str:
    """La réserve que la page fait sur elle-même, sortie de la prose et marquée
    comme un avertissement : c'est un gage de sérieux, pas une note de bas de
    page.
    """
    return (f'<div class="note avertissement">{icone("triangle-alert", "Attention")}'
            f'<div>{texte}</div></div>')


def pied() -> str:
    """Pied de page.

    Il porte ce que le lecteur doit savoir avant de citer un chiffre : que ce
    site est un document politique, d'où viennent ses données, et ce qu'il
    n'est pas. Il renvoie aussi aux objections : un programme qui ne publie
    pas ce qu'on lui oppose n'a pas de raison d'être cru. Un site qui réclame la transparence de l'État se doit d'être
    transparent sur lui-même.
    """
    return f"""<footer>
  <p><strong>Ce site est un document politique.</strong> Il est publié par le
  Parti libéral français : il défend une orientation, et le dit. Il n'émane
  d'aucune administration, ne constate aucune infraction et ne met personne en
  cause nommément.</p>
  <p>Les chiffres cités sont publics, datés et sourcés un par un sur la page
  <a href="sources.html">Sources</a> ; ils viennent d'administrations, de
  juridictions financières et d'organisations internationales. Beaucoup sont
  des <em>estimations</em> : quand deux méthodes officielles donnent deux
  résultats différents, nous donnons les deux. Six valeurs font exception — les
  hypothèses de notre chiffrage, qui ne peuvent venir de personne d'autre que
  nous ; elles sont isolées et nommées sur
  <a href="sources.html#hypotheses">Sources</a>, pour être contestées. Les objections qui nous sont faites sont rassemblées et traitées sur
  la page <a href="objections.html">Objections</a>. Dernière
  revue&nbsp;: {escape(REVUE)}.</p>
  <p>Textes et infographies sous
  <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC&nbsp;BY-SA&nbsp;4.0</a>,
  code du site sous licence Apache&nbsp;2.0. Tout est sur
  <a href="{DEPOT}">GitHub</a> : une erreur se signale, et se corrige.</p>
  <p>Un site du
  <a href="{SITE_PARENT}">Parti libéral français</a>.</p>
</footer>"""


def page(fichier: str, titre_onglet: str, description: str, corps: str) -> str:
    """La page complète, de ``<!doctype>`` au pied.

    ``theme-color`` reprend le vert du bandeau : sur un téléphone, la barre du
    navigateur prend cette couleur, et la page commence où elle commence.
    """
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0b3d3a">
<title>{escape(titre_onglet)}</title>
<meta name="description" content="{escape(description)}">
<link rel="icon" href="ressources/icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="ressources/icone.svg">
<link rel="stylesheet" href="ressources/style.css">
</head>
<body>
{entete(fichier)}
<main id="contenu" tabindex="-1">
{corps}
</main>
{pied()}
</body>
</html>
"""
