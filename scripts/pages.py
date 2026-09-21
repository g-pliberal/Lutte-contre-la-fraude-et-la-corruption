"""Le contenu des sept pages.

Une fonction par page, qui rend le corps de ``<main>`` ; le gabarit fait le
reste. Les chiffres sont tous datés et attribués : la page « Sources » tient la
liste complète, et chaque bloc renvoie à ce qui le concerne.

RÈGLE DE MAISON, et elle tient tout le site : quand deux sources officielles
donnent deux chiffres différents, on donne les deux et on dit que l'État
n'arbitre pas. C'est précisément l'argument.
"""

from gabarit import (affiche, cle, depliant, engagements, gestes, mesures,
                     page, plan, points, reperes, tableau, vigilance)


# ---------------------------------------------------------------------------
# 1. Le projet — l'affiche, les quatre engagements, la méthode
# ---------------------------------------------------------------------------

def accueil() -> str:
    corps = affiche(
        "Le programme",
        "La fraude prospère<br>là où l'État<br>"
        '<span class="cle-texte">est illisible</span>',
        "La France prélève plus que tout autre pays de l'Union européenne et "
        "dépense près de 1&nbsp;670&nbsp;milliards d'euros par an — sans publier "
        "le moindre chiffrage officiel de ce qui lui échappe. Notre programme "
        "tient en une phrase&nbsp;: rendre l'argent public traçable à l'euro "
        "près, et rendre la règle assez simple pour qu'on ne puisse plus s'y "
        "cacher.",
    )

    corps += """
<div class="note entree">
  <p>Ce site fait deux choses, et rien d'autre&nbsp;: il décrit <b>la politique
  que la France mène aujourd'hui</b> contre la fraude et la corruption — ses
  lois, ses agences, ses moyens, ses résultats — puis il propose <b>une
  alternative libérale</b>, mesure par mesure, avec son coût et ses limites.</p>
  <p class="actions">
    <a class="bouton" href="programme.html">Lire les dix mesures</a>
    <a class="bouton second" href="constat.html">Commencer par les chiffres</a>
  </p>
</div>
"""

    corps += engagements((
        ("100 %",
         "Chaque euro public publié en ligne, du contrat jusqu'au dernier "
         "avenant.",
         "Marchés, subventions, aides aux entreprises, dépenses des "
         "collectivités&nbsp;: en données ouvertes, lisibles par une machine, "
         "sous trente jours. Ce n'est pas une idée neuve — l'Ukraine "
         "(<i>Prozorro</i>) et les États-Unis (<i>USAspending</i>) le font "
         "déjà. La France publie aujourd'hui des fragments, dans des formats "
         "qui ne se recoupent pas."),
        ("1 par an",
         "Un chiffrage officiel et indépendant de la fraude, publié chaque "
         "année.",
         "Le Royaume-Uni publie son <i>tax gap</i> depuis 2005&nbsp;: une "
         "méthode, une série, un débat. La France n'a jamais publié "
         "d'estimation officielle consolidée — les chiffres qui circulent "
         "viennent d'un syndicat, d'un institut ou d'une commission, et vont "
         "de 9 à 100&nbsp;milliards d'euros selon le périmètre retenu."),
        ("30 %",
         "Jusqu'à 30&nbsp;% des sommes recouvrées pour qui fait tomber une "
         "fraude.",
         "C'est le barème du programme de la <i>Securities and Exchange "
         "Commission</i> américaine, étendu ici à la fraude fiscale, sociale "
         "et aux marchés publics. La France a bien un « aviseur fiscal » "
         "depuis 2017, mais son indemnisation reste discrétionnaire, "
         "confidentielle et sans barème public."),
        ("0",
         "Zéro marché public attribué sans que le contrat soit publié d'abord.",
         "La commande publique pèse de l'ordre de 160&nbsp;milliards d'euros "
         "par an. C'est le premier lieu de la corruption ordinaire, et le "
         "relèvement répété des seuils de gré à gré l'a rendu moins visible, "
         "pas plus honnête."),
    ))

    corps += "<h2>Notre méthode&nbsp;: trois gestes, dans cet ordre</h2>"
    corps += gestes((
        "<strong>Assécher.</strong> Une règle illisible est une règle qu'on "
        "contourne, et près de 470 dépenses fiscales font une règle illisible. "
        "Assiette large, taux bas, moins d'exceptions&nbsp;: la première "
        "politique anti-fraude est une politique fiscale.",
        "<strong>Exposer.</strong> Ce qui est public doit être public. La "
        "dépense, les contrats, les bénéficiaires effectifs des sociétés, les "
        "intérêts des décideurs&nbsp;: en ligne, en format ouvert, sans "
        "demander la permission.",
        "<strong>Recouvrer.</strong> Une sanction annoncée et jamais encaissée "
        "ne dissuade personne. Ce qui compte n'est pas le montant notifié, "
        "c'est le montant rentré — et il faut le publier, service par service.",
    ))

    corps += points((
        ("Ce n'est pas une affaire de moyens seulement",
         "Ajouter des contrôleurs à un code fiscal de plusieurs milliers de "
         "pages "
         "revient à embaucher des traducteurs pour un texte que personne "
         "n'écrit lisiblement. Les moyens comptent&nbsp;: ils ne suffisent "
         "pas, et l'histoire des vingt dernières années le montre."),
        ("Ce n'est pas un procès fait aux pauvres",
         "La fraude aux prestations sociales existe et doit être combattue. "
         "Mais les ordres de grandeur connus la placent loin derrière la "
         "fraude aux prélèvements&nbsp;: refuser de le dire, c'est se tromper "
         "de cible — et le non-recours aux prestations pèse, lui aussi, "
         "plusieurs milliards."),
        ("Ce n'est pas un ministère de plus",
         "La France compte déjà une agence anticorruption, une haute "
         "autorité, un parquet national financier, une cellule de "
         "renseignement financier et une mission interministérielle. Nous n'en "
         "créons aucune&nbsp;: nous proposons de leur donner l'indépendance et "
         "les données qui leur manquent."),
    ))

    corps += vigilance(
        "<b>Aucun des chiffres de ce site n'est de nous, et aucun n'est "
        "certain.</b> La fraude se mesure mal par nature&nbsp;: on n'observe "
        "que ce qu'on détecte. Les estimations que nous citons viennent "
        "d'administrations, de juridictions financières ou d'organisations "
        "internationales ; elles sont datées, attribuées, et parfois "
        "contradictoires entre elles. Quand c'est le cas, nous donnons les "
        "deux chiffres plutôt que celui qui nous arrange — et c'est justement "
        "ce désordre que notre deuxième engagement propose de faire cesser."
    )

    corps += """
<div class="creme">
  <p class="surtitre">La suite</p>
  <h2 class="serif" style="text-transform:none">Six pages, et l'on a fait le tour</h2>
  <p><a href="constat.html"><b>Constat</b></a> — ce que l'on sait et ce que
  l'on ne sait pas de la fraude et de la corruption en France, chiffre par
  chiffre.<br>
  <a href="dispositif.html"><b>Dispositif</b></a> — la politique actuelle&nbsp;:
  trente ans de textes, quatorze institutions, ce qu'elles font et ce
  qu'elles obtiennent.<br>
  <a href="diagnostic.html"><b>Diagnostic</b></a> — pourquoi ce dispositif
  plafonne, en sept causes.<br>
  <a href="programme.html"><b>Programme</b></a> — les dix mesures, et ce que
  chacune remplace.<br>
  <a href="chiffrage.html"><b>Chiffrage</b></a> — ce que cela coûte, ce que
  cela peut rapporter, et notre degré de confiance dans chaque ligne.<br>
  <a href="sources.html"><b>Sources</b></a> — tout ce qui est cité, avec le
  lien et la date.</p>
</div>
"""
    return page(
        "index.html",
        "Lutte contre la fraude et la corruption — le programme du Parti libéral français",
        "La politique française de lutte contre la fraude et la corruption, "
        "décrite et chiffrée, et l'alternative libérale que nous proposons : "
        "traçabilité intégrale de l'argent public, simplification fiscale, "
        "indépendance des poursuites.",
        corps,
    )


# ---------------------------------------------------------------------------
# 2. Constat — ce que l'on sait, et ce que l'on ne sait pas
# ---------------------------------------------------------------------------

def constat() -> str:
    corps = affiche(
        "Le constat",
        "Personne ne sait<br>combien la France<br>"
        '<span class="cle-texte">perd chaque année</span>',
        "Ce n'est pas une formule&nbsp;: aucune administration française ne "
        "publie d'estimation officielle et consolidée de la fraude. Les "
        "chiffres qui circulent viennent d'un syndicat, d'un institut de "
        "statistique, d'une commission ou d'une caisse — et vont de 9 à "
        "100&nbsp;milliards d'euros selon le périmètre retenu. Voici ce qu'ils "
        "disent, avec leur date et leur périmètre.",
    )

    corps += plan((
        ("fiscale", "Fraude fiscale"),
        ("controle", "Ce que le contrôle rapporte"),
        ("sociale", "Fraude sociale"),
        ("corruption", "Corruption"),
        ("marches", "Marchés publics"),
        ("trou", "Ce que l'on ignore"),
    ))

    corps += reperes((
        ("Ce qui échapperait au fisc", "60 à 100 Md €",
         "Fourchette la plus citée dans le débat public&nbsp;: estimation "
         "syndicale de 2019, jamais reprise à son compte par l'État."),
        ("Ce que le contrôle fiscal notifie", "≈ 15 Md €",
         "Par an, droits et pénalités. Environ 70&nbsp;% seulement finissent "
         "encaissés en 2023 (DGFiP)."),
        ("Cotisations sociales éludées", "6,8 à 8,4 Md €",
         "Par an, essentiellement du travail dissimulé "
         "(Haut Conseil du financement de la protection sociale, 2022)."),
        ("Perception de la corruption", "67 / 100",
         "Note de la France en 2024, 25ᵉ rang mondial&nbsp;; elle était de "
         "71/100 et 20ᵉ en 2023 (Transparency International)."),
    ))

    corps += cle(
        "Combien coûte la fraude fiscale ?",
        "Cinq sources publiques, quatre chiffres, un refus de chiffrer — et "
        "aucun arbitrage de l'État. "
        "L'écart n'est pas seulement statistique&nbsp;: les <b>périmètres</b> "
        "diffèrent, et personne n'est chargé de les réconcilier.",
        tableau(
            "Estimations publiques de la fraude fiscale en France",
            ("Source", "Millésime", "Périmètre", "Estimation"),
            (
                ("Solidaires Finances Publiques", "2019", "Fraude fiscale, tous impôts",
                 "80 à 100 Md&nbsp;€/an"),
                ("Conseil des prélèvements obligatoires", "2007",
                 "Fraude aux prélèvements obligatoires", "29 à 40 Md&nbsp;€/an"),
                ("Insee", "2022 (année 2012)", "TVA seule", "20 à 25 Md&nbsp;€"),
                ("Commission européenne, <i>VAT&nbsp;Gap</i>", "2023 (année 2021)",
                 "TVA seule, fraude <b>et</b> erreurs et défaillances",
                 "≈ 9 Md&nbsp;€, soit ≈ 5&nbsp;% des recettes théoriques"),
                ("Cour des comptes", "2023", "Fraude fiscale",
                 "Aucun chiffrage&nbsp;: la Cour constate qu'il n'existe pas "
                 "d'estimation fiable et récente"),
            ),
            ("texte", "date", "long", "long"),
        ),
        "Les périmètres ne se recouvrent pas et les millésimes s'échelonnent "
        "sur quinze ans&nbsp;: ce tableau ne dit pas laquelle de ces "
        "estimations est juste, il dit qu'aucune institution n'est chargée de "
        "le trancher. Voir <a href=\"sources.html#fiscal\">Sources</a>.",
        "fiscale",
    )

    corps += cle(
        "Le contrôle fiscal rapporte-t-il ?",
        "Il notifie de l'ordre de 15&nbsp;milliards d'euros par an et en "
        "encaisse environ 10. <b>L'écart d'un tiers est structurel</b>, et "
        "c'est lui qu'il faudrait suivre&nbsp;: un redressement annoncé et "
        "jamais recouvré ne finance rien.",
        tableau(
            "Contrôle fiscal : droits et pénalités notifiés puis encaissés (ordres de grandeur)",
            ("Année", "Notifié", "Encaissé", "Part encaissée"),
            (
                ("2019", "≈ 13,9 Md&nbsp;€", "≈ 11,0 Md&nbsp;€", "≈ 79&nbsp;%"),
                ("2020 <span class=\"discret\">(covid)</span>", "≈ 10,2 Md&nbsp;€",
                 "≈ 7,8 Md&nbsp;€", "≈ 76&nbsp;%"),
                ("2021", "≈ 13,4 Md&nbsp;€", "≈ 10,7 Md&nbsp;€", "≈ 80&nbsp;%"),
                ("2022", "≈ 14,6 Md&nbsp;€", "≈ 10,6 Md&nbsp;€", "≈ 73&nbsp;%"),
                ("2023", "≈ 15,2 Md&nbsp;€", "≈ 10,6 Md&nbsp;€", "≈ 70&nbsp;%"),
            ),
            ("date", "nombre", "nombre", "nombre"),
        ),
        "Ordres de grandeur arrondis, tels qu'ils ressortent des rapports "
        "d'activité et des communiqués annuels de la DGFiP&nbsp;; les "
        "périmètres de publication ont évolué sur la période, et les montants "
        "encaissés une année donnée portent en partie sur des contrôles "
        "antérieurs. À lire comme une tendance, pas comme une comptabilité.",
        "controle",
    )

    corps += cle(
        "Et la fraude sociale ?",
        "Elle est réelle, et elle est <b>plus petite d'un ordre de grandeur</b> "
        "que la fraude aux prélèvements. Le dire n'est pas l'excuser&nbsp;: "
        "c'est refuser de se tromper de cible.",
        tableau(
            "Fraude sociale : estimations et montants détectés",
            ("Poste", "Source", "Nature", "Montant"),
            (
                ("Cotisations sociales éludées", "HCFiPS, 2022",
                 "Estimation (travail dissimulé)", "6,8 à 8,4 Md&nbsp;€/an"),
                ("Prestations familiales et RSA", "CNAF",
                 "Préjudice estimé par la caisse", "≈ 2,5 à 3 Md&nbsp;€/an"),
                ("Assurance maladie", "CNAM",
                 "Fraude <b>détectée et stoppée</b>", "≈ 0,5 Md&nbsp;€ en 2023"),
                ("Toutes branches", "Ministère des comptes publics",
                 "Fraude <b>détectée et stoppée</b>", "≈ 2,1 Md&nbsp;€ en 2023"),
                ("<b>Pour mémoire&nbsp;:</b> non-recours au RSA", "DREES, 2022",
                 "Droits non réclamés par des allocataires éligibles",
                 "≈ 34&nbsp;% des éligibles chaque trimestre"),
            ),
            ("texte", "texte", "long", "nombre"),
        ),
        "La dernière ligne n'est pas une provocation&nbsp;: un système que "
        "l'on rend plus contrôlable doit l'être dans les deux sens, et un tiers "
        "d'allocataires qui ne réclament pas ce à quoi ils ont droit est le "
        "symptôme de la même complexité. Voir "
        "<a href=\"sources.html#social\">Sources</a>.",
        "sociale",
    )

    corps += cle(
        "La France est-elle corrompue ?",
        "Pas au sens des pays où l'on paie un pot-de-vin au guichet. Mais sa "
        "note se dégrade, et les évaluateurs internationaux lui reprochent "
        "toujours les mêmes choses&nbsp;: <b>les nominations, le pantouflage, "
        "le contrôle de l'exécutif sur les poursuites</b>.",
        tableau(
            "Indice de perception de la corruption de la France (Transparency International)",
            ("Millésime", "Note sur 100", "Rang mondial"),
            (
                ("2019", "69", "23ᵉ"),
                ("2020", "69", "23ᵉ"),
                ("2021", "71", "22ᵉ"),
                ("2022", "72", "21ᵉ"),
                ("2023", "71", "20ᵉ"),
                ("2024", "67", "25ᵉ"),
            ),
            ("date", "nombre", "nombre"),
        )
        + "<p>L'indice mesure une <b>perception</b> par des experts et des "
        "milieux d'affaires, pas un nombre d'actes&nbsp;: il ne dit pas "
        "combien on vole, il dit ce que l'on croit. C'est une limite, et elle "
        "vaut d'être écrite. Deux autres signaux la complètent&nbsp;:</p>"
        "<p>— le <b>GRECO</b>, organe anticorruption du Conseil de l'Europe, "
        "classe la France en conformité seulement <i>partielle</i> sur la "
        "majorité des recommandations de son cinquième cycle, qui porte sur "
        "les hautes fonctions de l'exécutif et les services répressifs&nbsp;;<br>"
        "— la justice prononce de l'ordre de <b>250 à 300 condamnations par "
        "an</b> pour atteintes à la probité — corruption, favoritisme, prise "
        "illégale d'intérêts, détournement de fonds publics —, un chiffre "
        "stable et sans commune mesure avec les estimations de l'ampleur du "
        "phénomène.</p>",
        "Dernier millésime repris ici&nbsp;: 2024. Voir "
        "<a href=\"sources.html#corruption\">Sources</a>.",
        "corruption",
    )

    corps += cle(
        "Où la corruption se joue-t-elle ?",
        "Dans la <b>commande publique</b>, d'abord&nbsp;: de l'ordre de "
        "160&nbsp;milliards d'euros par an, près de 6&nbsp;% du PIB, et le "
        "premier poste de risque identifié par toutes les évaluations.",
        "<p>La Commission européenne estimait en 2014 le coût de la corruption "
        "pour l'Union à environ <b>120&nbsp;milliards d'euros par an</b>&nbsp;; "
        "une étude du Parlement européen de 2016, retenant un périmètre plus "
        "large, aboutissait à une fourchette de <b>179 à 990&nbsp;milliards</b>. "
        "L'écart de un à huit entre deux travaux européens — l'un de la "
        "Commission, l'autre du Parlement — dit l'état réel de la "
        "connaissance.</p>"
        "<p>Trois traits rendent le risque français particulier&nbsp;:</p>"
        "<p>— les <b>seuils de dispense de publicité</b> ont été relevés à "
        "plusieurs reprises depuis 2020, jusqu'à 100&nbsp;000&nbsp;€ pour "
        "certains marchés de travaux&nbsp;: autant de contrats attribués sans "
        "mise en concurrence formelle&nbsp;;<br>"
        "— les <b>données de la commande publique</b> sont publiées, mais "
        "incomplètes, tardives et dispersées entre profils d'acheteurs&nbsp;;<br>"
        "— les <b>avenants</b>, qui font souvent le vrai prix d'un marché, ne "
        "sont pas systématiquement publiés.</p>",
        "Voir <a href=\"sources.html#marches\">Sources</a>.",
        "marches",
    )

    corps += '<h2 id="trou" tabindex="-1">Ce que l\'on ignore, et qui n\'est pas rien</h2>'
    corps += """
<p>Un constat honnête doit dire où il s'arrête. Sur les cinq questions
ci-dessus, voici ce qu'aucune source publique française ne permet de
répondre aujourd'hui&nbsp;:</p>
"""
    corps += tableau(
        "Les angles morts de la statistique publique française",
        ("Question", "État de la connaissance"),
        (
            ("Quel est l'écart entre l'impôt dû et l'impôt perçu&nbsp;?",
             "Aucune estimation officielle, aucune série. Le Royaume-Uni la "
             "publie chaque année depuis 2005, l'Italie, la Suède et les "
             "États-Unis également."),
            ("Combien de fraude est détectée, rapportée à la fraude commise&nbsp;?",
             "Inconnu, faute de dénominateur. On publie le numérateur — les "
             "montants détectés — et on l'appelle un résultat."),
            ("Quel est le taux de recouvrement effectif, service par service&nbsp;?",
             "Agrégé au niveau national, jamais détaillé publiquement."),
            ("Combien coûtent les 470 dépenses fiscales, et lesquelles sont "
             "détournées&nbsp;?",
             "Le coût est publié chaque année dans l'annexe « Voies et moyens » "
             "du budget&nbsp;; l'évaluation de leur efficacité et de leur "
             "détournement, non."),
            ("Qui détient réellement les sociétés françaises&nbsp;?",
             "Le registre des bénéficiaires effectifs existe, mais son accès "
             "public a été restreint après un arrêt de la Cour de justice de "
             "l'Union européenne de novembre 2022."),
        ),
        ("long", "long"),
    )

    corps += vigilance(
        "<b>Une estimation n'est pas une mesure.</b> Toute la difficulté de "
        "cette page tient en une phrase&nbsp;: on ne connaît que la fraude que "
        "l'on a détectée, et détecter davantage fait monter les chiffres sans "
        "que la fraude ait bougé. C'est pourquoi nous ne prétendons pas "
        "« récupérer 100&nbsp;milliards » — et pourquoi notre premier "
        "engagement porte sur la mesure elle-même."
    )

    return page(
        "constat.html",
        "Constat — fraude et corruption en France, ce que disent les chiffres",
        "Les estimations publiques de la fraude fiscale, sociale et de la "
        "corruption en France : leurs sources, leurs dates, leurs périmètres — "
        "et leurs contradictions.",
        corps,
    )


# ---------------------------------------------------------------------------
# 3. Dispositif — la politique que la France mène aujourd'hui
# ---------------------------------------------------------------------------

def dispositif() -> str:
    corps = affiche(
        "La politique actuelle",
        "Trente ans de lois,<br>quatorze institutions,<br>"
        '<span class="cle-texte">et un plafond</span>',
        "La France n'a pas rien fait&nbsp;: depuis la loi Sapin&nbsp;I de 1993, "
        "chaque scandale a produit sa loi et souvent son agence. Le dispositif "
        "existe, il est dense, et il est honnêtement tenu par des gens "
        "compétents. Cette page le décrit tel qu'il est — avant de dire, page "
        "suivante, pourquoi il plafonne.",
    )

    corps += plan((
        ("chronologie", "Trente ans de lois"),
        ("institutions", "Qui fait quoi"),
        ("resultats", "Ce que cela donne"),
        ("juge", "Ce qui marche"),
    ))

    corps += reperes((
        ("Textes majeurs depuis 1993", "11",
         "Huit lois, de Sapin&nbsp;I à la loi de finances pour 2024, un "
         "décret, un plan gouvernemental et la mise en place du Parquet "
         "européen."),
        ("Administrations et autorités mobilisées", "≈ 14",
         "Deux ministères, quatre autorités ou agences, trois réseaux "
         "juridictionnels, cinq caisses."),
        ("Amendes des conventions judiciaires", "≈ 4 Md €",
         "Cumul des CJIP conclues depuis 2016, dont 2,08&nbsp;Md&nbsp;€ pour "
         "la seule affaire Airbus (2020)."),
        ("Agents promis au contrôle fiscal", "+ 1 500",
         "D'ici 2027, annoncés par le plan antifraude de mai 2023 — après une "
         "décennie de baisse des effectifs."),
    ))

    corps += '<h2 id="chronologie" tabindex="-1">Trente ans de lois, une par scandale</h2>'
    corps += """
<p>La séquence est toujours la même&nbsp;: une affaire, une indignation, une
loi, une agence. Ce n'est pas une critique en soi — plusieurs de ces textes ont
réellement changé les choses. Mais l'empilement a un prix, et il se paie en
lisibilité.</p>
"""
    corps += tableau(
        "Les principaux textes français contre la fraude et la corruption",
        ("Date", "Texte", "Ce qu'il crée ou change"),
        (
            ("1993", "Loi Sapin&nbsp;I",
             "Transparence des procédures de la commande publique et du "
             "financement de la vie politique. Le socle&nbsp;: publicité et "
             "mise en concurrence."),
            ("2010", "Loi du 9 juillet 2010",
             "Crée l'AGRASC&nbsp;: l'État sait enfin saisir, gérer et "
             "confisquer les avoirs issus d'infractions."),
            ("2013", "Lois du 11 octobre 2013",
             "Après l'affaire Cahuzac&nbsp;: déclarations d'intérêts et de "
             "patrimoine, et la Haute Autorité pour la transparence de la vie "
             "publique (HATVP) pour les vérifier."),
            ("2013", "Loi du 6 décembre 2013",
             "Crée le parquet national financier (PNF) et durcit les peines "
             "en matière de fraude fiscale aggravée."),
            ("2016", "Loi Sapin&nbsp;II",
             "Le texte pivot&nbsp;: Agence française anticorruption (AFA), "
             "obligation de programme de conformité pour les grandes "
             "entreprises, convention judiciaire d'intérêt public (CJIP), "
             "répertoire des représentants d'intérêts, premier statut du "
             "lanceur d'alerte."),
            ("2018", "Loi du 23 octobre 2018",
             "Service d'enquêtes judiciaires des finances, publication des "
             "sanctions fiscales des personnes morales, assouplissement du "
             "« verrou de Bercy », statut de l'aviseur fiscal indemnisé."),
            ("2020", "Décret créant la MICAF",
             "Mission interministérielle de coordination antifraude, avec des "
             "comités départementaux (CODAF) chargés de faire parler entre "
             "eux fisc, URSSAF, police et caisses."),
            ("2021", "Parquet européen",
             "Des procureurs européens délégués en France poursuivent "
             "directement les atteintes au budget de l'Union."),
            ("2022", "Loi Waserman du 21 mars 2022",
             "Transpose la directive européenne de 2019&nbsp;: définition "
             "élargie du lanceur d'alerte, protection contre les représailles, "
             "irresponsabilité pénale pour la soustraction de documents."),
            ("2023", "Plan antifraude de mai 2023",
             "1&nbsp;500 agents supplémentaires au contrôle fiscal d'ici 2027, "
             "doublement des contrôles sur les plus hauts patrimoines, "
             "conseil d'évaluation des fraudes."),
            ("2024", "Loi de finances pour 2024",
             "Crée le délit de mise à disposition d'instruments de fraude "
             "fiscale et étend les possibilités d'enquête sous pseudonyme."),
        ),
        ("date", "texte", "long"),
    )

    corps += '<h2 id="institutions" tabindex="-1">Qui fait quoi</h2>'
    corps += """
<p>Quatorze entités, trois ministères de tutelle, et des périmètres qui se
recoupent. Le tableau ci-dessous donne pour chacune sa mission et l'ordre de
grandeur de ses moyens&nbsp;: c'est la comparaison entre les deux dernières
colonnes qui est instructive.</p>
"""
    corps += tableau(
        "Le dispositif français, entité par entité (ordres de grandeur)",
        ("Entité", "Depuis", "Mission", "Moyens"),
        (
            ("DGFiP — contrôle fiscal", "—",
             "Contrôle et recouvrement de l'impôt",
             "≈ 10&nbsp;000 agents dédiés au contrôle, contre ≈ 13&nbsp;000 "
             "au début des années 2010"),
            ("TRACFIN", "1990",
             "Cellule de renseignement financier&nbsp;: reçoit les "
             "déclarations de soupçon des banques, notaires, casinos",
             "≈ 200 agents&nbsp;; plus de 180&nbsp;000 informations reçues "
             "par an, quelques milliers de notes transmises"),
            ("SEJF", "2019",
             "Service d'enquêtes judiciaires des finances — la « police "
             "fiscale et douanière »",
             "≈ 300 agents, officiers fiscaux et douaniers judiciaires"),
            ("URSSAF", "—",
             "Contrôle des cotisations, lutte contre le travail dissimulé",
             "≈ 1&nbsp;Md&nbsp;€ de redressements pour travail dissimulé par an"),
            ("CNAF, CNAM, CNAV, MSA", "—",
             "Contrôle des prestations versées",
             "≈ 2,1&nbsp;Md&nbsp;€ de fraude détectée et stoppée en 2023, "
             "toutes branches"),
            ("PNF", "2014",
             "Parquet national financier&nbsp;: poursuites en matière de "
             "corruption, fraude fiscale complexe, atteintes à la probité",
             "≈ 20 magistrats pour plusieurs centaines de procédures"),
            ("OCLCIFF", "2013",
             "Office central de lutte contre la corruption et les infractions "
             "financières et fiscales — les enquêteurs du PNF",
             "≈ 100 enquêteurs"),
            ("JIRS", "2004",
             "Huit juridictions interrégionales spécialisées en criminalité "
             "organisée et délinquance financière", "Magistrats spécialisés"),
            ("AFA", "2017",
             "Agence française anticorruption&nbsp;: contrôle les programmes "
             "de conformité des entreprises et des acteurs publics, conseille, "
             "forme", "≈ 50 agents"),
            ("HATVP", "2014",
             "Déclarations d'intérêts et de patrimoine, répertoire des "
             "représentants d'intérêts, contrôle déontologique des départs "
             "vers le privé", "≈ 60 agents pour ≈ 16&nbsp;000 déclarants"),
            ("AGRASC", "2011",
             "Gestion et recouvrement des avoirs saisis et confisqués",
             "Effectif restreint&nbsp;; plusieurs centaines de millions "
             "d'euros d'avoirs gérés"),
            ("Cour des comptes et CRTC", "1807",
             "Contrôle de la régularité et de l'efficacité de la dépense "
             "publique, signalement au parquet", "≈ 1&nbsp;800 agents"),
            ("MICAF", "2020",
             "Coordination interministérielle&nbsp;: fait travailler ensemble "
             "fisc, douane, URSSAF, caisses, police, justice",
             "Équipe restreinte, adossée à ≈ 100 comités départementaux"),
            ("Parquet européen", "2021",
             "Poursuite des atteintes au budget de l'Union européenne",
             "Quelques procureurs européens délégués en France"),
        ),
        ("texte", "date", "long", "long"),
    )

    corps += """
<p class="discret">La colonne « Depuis » donne l'année d'<b>installation
effective</b>, qui suit en général d'un an la loi qui crée l'entité&nbsp;: le
PNF et la HATVP sont créés par les lois de 2013 et installés en 2014, l'AFA par
la loi de 2016 et installée en 2017, l'AGRASC par la loi de 2010 et installée
en 2011.</p>
"""
    corps += '<h2 id="resultats" tabindex="-1">Ce que cela donne</h2>'
    corps += """
<p>Trois résultats, et leur envers. Nous les prenons dans l'ordre où
l'administration les met en avant.</p>
"""
    corps += points((
        ("Le contrôle fiscal tient",
         "≈ 15&nbsp;Md&nbsp;€ notifiés par an, en hausse depuis 2020. "
         "<b>Mais</b> environ un tiers n'est jamais encaissé, et ce montant "
         "rapporté aux estimations basses de la fraude reste minoritaire."),
        ("Les grandes entreprises transigent",
         "Une quarantaine de CJIP depuis 2016, ≈ 4&nbsp;Md&nbsp;€ d'amendes. "
         "<b>Mais</b> la convention éteint les poursuites sans reconnaissance "
         "de culpabilité, et n'entraîne pas d'exclusion des marchés publics."),
        ("La coordination existe enfin",
         "La MICAF et les CODAF ont mis fin à l'époque où le fisc et l'URSSAF "
         "ne se parlaient pas. <b>Mais</b> la coordination porte sur les "
         "dossiers, pas sur les données&nbsp;: il n'existe toujours pas de vue "
         "d'ensemble publiable."),
    ))

    corps += cle(
        "Ce qui marche, et qu'il faut garder",
        "Un programme sérieux commence par dire ce qu'il ne détruira pas. "
        "Quatre briques du dispositif actuel sont bonnes&nbsp;; notre "
        "proposition les conserve et les étend.",
        "<p><b>La CJIP.</b> Elle a permis de sanctionner en trois ans plus que "
        "la justice pénale classique en vingt, et de rapatrier en France des "
        "amendes que les parquets américains encaissaient auparavant à notre "
        "place. Nous la gardons — en la rendant entièrement publique et en "
        "l'assortissant d'une exclusion temporaire des marchés.</p>"
        "<p><b>TRACFIN.</b> Une cellule de renseignement financier reconnue "
        "par ses homologues, qui traite un flux considérable avec peu de "
        "moyens. Nous proposons de l'étoffer, pas de la réformer.</p>"
        "<p><b>La HATVP.</b> Le contrôle des déclarations d'intérêts et le "
        "répertoire des représentants d'intérêts sont des acquis de 2013 et "
        "2016 qu'il serait absurde de défaire. Nous proposons d'en durcir les "
        "suites, pas d'en réduire le champ.</p>"
        "<p><b>L'AGRASC.</b> Saisir puis confisquer est ce qui dissuade "
        "réellement&nbsp;: c'est la seule sanction qui touche au produit de "
        "l'infraction. Nous proposons d'élargir son périmètre à la fraude "
        "fiscale et sociale organisée.</p>",
        "",
        "juge",
    )

    corps += depliant(
        "Et l'Europe dans tout cela ?",
        "<p>Trois instruments européens comptent, et pèsent souvent plus que "
        "le droit national&nbsp;:</p>"
        "<p><b>Le Parquet européen</b> (2021) poursuit directement les "
        "atteintes au budget de l'Union — fraude aux subventions, fraude à la "
        "TVA de plus de 10&nbsp;M&nbsp;€ — sans passer par les parquets "
        "nationaux. C'est la première juridiction supranationale de poursuite, "
        "et elle fonctionne.</p>"
        "<p><b>Les directives anti-blanchiment</b> imposent le registre des "
        "bénéficiaires effectifs des sociétés. La Cour de justice de l'Union "
        "européenne a jugé en novembre&nbsp;2022 que l'accès du grand public à "
        "ce registre portait une atteinte disproportionnée à la vie "
        "privée&nbsp;; depuis, l'accès a été restreint en France comme "
        "ailleurs. Le nouveau paquet anti-blanchiment adopté en 2024 rétablit "
        "un accès pour les journalistes et la société civile justifiant d'un "
        "intérêt légitime.</p>"
        "<p><b>La directive de 2019 sur les lanceurs d'alerte</b>, transposée "
        "en France par la loi du 21&nbsp;mars 2022, est le texte le plus "
        "protecteur d'Europe sur le papier. Sa faiblesse est ailleurs&nbsp;: "
        "elle protège contre les représailles, elle ne compense rien.</p>",
    )

    return page(
        "dispositif.html",
        "Dispositif — la politique française contre la fraude et la corruption",
        "Les onze textes majeurs, les quatorze institutions et les moyens "
        "réels de la "
        "politique française de lutte contre la fraude et la corruption, de la "
        "loi Sapin I au plan antifraude de 2023.",
        corps,
    )


# ---------------------------------------------------------------------------
# 4. Diagnostic — pourquoi le dispositif plafonne
# ---------------------------------------------------------------------------

def diagnostic() -> str:
    corps = affiche(
        "L'analyse",
        "On a multiplié<br>les gendarmes.<br>"
        '<span class="cle-texte">Pas la clarté.</span>',
        "Sept causes, et une seule idée derrière&nbsp;: un État qui écrit des "
        "règles illisibles, prélève au taux le plus élevé d'Europe, garde ses "
        "données pour lui et contrôle ses propres poursuites fabrique de la "
        "fraude plus vite qu'il n'en réprime.",
    )

    corps += plan((
        ("complexite", "La complexité"),
        ("taux", "Le taux"),
        ("recouvrement", "Le recouvrement"),
        ("opacite", "L'opacité"),
        ("poursuites", "Les poursuites"),
        ("moyens", "Les moyens"),
        ("alerte", "L'alerte"),
    ))

    corps += reperes((
        ("Dépenses fiscales recensées", "≈ 470",
         "Pour plus de 80&nbsp;Md&nbsp;€ par an&nbsp;: autant de régimes "
         "particuliers, autant de frontières à contourner "
         "(annexe « Voies et moyens » du budget)."),
        ("Taux de prélèvements obligatoires", "≈ 43 % du PIB",
         "Le plus élevé de l'Union européenne avec le Danemark (Eurostat)."),
        ("Part des redressements jamais encaissée", "≈ 1/3",
         "Chaque année, de façon structurelle (DGFiP)."),
        ("Registre des bénéficiaires effectifs", "fermé",
         "Accès public restreint depuis l'arrêt de la CJUE de "
         "novembre&nbsp;2022."),
    ))

    corps += cle(
        "1. Une règle illisible est une règle qu'on contourne",
        "La fraude n'est pas seulement un choix moral&nbsp;: c'est souvent un "
        "<b>arbitrage de frontière</b>. Plus il y a de régimes particuliers, "
        "plus il y a de frontières, et plus il est facile de se ranger du bon "
        "côté d'une ligne qu'on a soi-même dessinée.",
        "<p>Près de 470 dépenses fiscales, plus de 80&nbsp;milliards d'euros "
        "par an, un code général des impôts de plusieurs milliers de pages, un "
        "code du travail et un code de la sécurité sociale du même ordre. À "
        "chaque niche correspond une définition, à chaque définition une zone "
        "grise, et à chaque zone grise une industrie du conseil dont le métier "
        "est de s'y loger.</p>"
        "<p>Le même mécanisme joue sur le versant social&nbsp;: la "
        "multiplication des statuts — salarié, auto-entrepreneur, "
        "micro-entreprise, portage, plateformes — a créé des différentiels de "
        "cotisation de plusieurs dizaines de points pour un travail identique. "
        "Le travail dissimulé n'est pas une déviance marginale dans ce "
        "contexte&nbsp;: c'est la forme extrême d'un arbitrage que la règle "
        "elle-même propose.</p>"
        "<p class=\"discret\">Corollaire rarement dit&nbsp;: la complexité "
        "produit aussi de la <b>fraude involontaire</b>, et des redressements "
        "qui frappent des contribuables de bonne foi. Les deux problèmes ont "
        "la même cause.</p>",
        "",
        "complexite",
    )

    corps += cle(
        "2. Le taux appelle la fraude",
        "Ce n'est pas une excuse, c'est une régularité&nbsp;: <b>plus le taux "
        "marginal est élevé, plus le gain espéré de la dissimulation est "
        "grand</b>, à probabilité de contrôle inchangée. La France prélève "
        "environ 43&nbsp;% du PIB, le plus haut niveau de l'Union.",
        "<p>Cette mécanique est connue depuis les travaux d'Allingham et "
        "Sandmo (1972) et elle a été vérifiée dans de nombreux pays&nbsp;: la "
        "fraude répond au produit « gain attendu × probabilité d'impunité ». "
        "Un État qui veut la réduire dispose donc de trois leviers, et non "
        "d'un seul&nbsp;: baisser le gain, augmenter la probabilité de "
        "détection, augmenter la sanction.</p>"
        "<p>La France n'actionne, depuis trente ans, que les deux "
        "derniers — et encore, imparfaitement. Le premier est traité comme un "
        "sujet tabou, alors qu'il est le seul dont l'effet ne dépend ni du "
        "nombre de contrôleurs ni de l'encombrement des tribunaux.</p>",
        "",
        "taux",
    )

    corps += cle(
        "3. On notifie, on n'encaisse pas",
        "Chaque année, l'administration annonce un montant de redressements. "
        "Chaque année, <b>environ un tiers n'est jamais recouvré</b> — "
        "entreprises liquidées, avoirs déplacés, contentieux qui s'éternisent. "
        "Le chiffre annoncé n'est pas le chiffre rentré.",
        "<p>Le problème est d'abord un problème d'indicateur. L'administration "
        "est jugée sur ce qu'elle notifie&nbsp;; elle publie donc ce qu'elle "
        "notifie. Le taux d'encaissement effectif, lui, n'est pas détaillé "
        "service par service, ni suivi dans le temps par une série publique.</p>"
        "<p>Le même travers joue en matière pénale&nbsp;: une amende "
        "prononcée, une confiscation ordonnée et un préjudice réparé sont "
        "trois choses différentes, et seule la première est annoncée le jour "
        "du jugement.</p>",
        "",
        "recouvrement",
    )

    corps += cle(
        "4. La transparence a reculé",
        "C'est le point le plus contre-intuitif de ce diagnostic&nbsp;: sur "
        "plusieurs fronts, <b>la France sait moins bien qu'il y a cinq ans qui "
        "détient quoi</b>.",
        "<p><b>Les bénéficiaires effectifs.</b> Depuis l'arrêt de la Cour de "
        "justice de l'Union européenne de novembre&nbsp;2022, l'accès du grand "
        "public au registre des bénéficiaires effectifs des sociétés est "
        "restreint. La décision protège un droit réel — la vie privée — mais "
        "elle a privé journalistes, chercheurs et ONG de l'outil qui avait "
        "permis la plupart des révélations de la décennie.</p>"
        "<p><b>La commande publique.</b> Les données existent, mais dispersées "
        "entre des centaines de profils d'acheteurs, publiées avec retard, "
        "dans des formats hétérogènes, et sans les avenants — qui font "
        "pourtant souvent le vrai prix d'un marché.</p>"
        "<p><b>Les aides aux entreprises.</b> Plusieurs dizaines de milliards "
        "d'euros par an, répartis entre des centaines de dispositifs, sans "
        "base unique consultable ligne à ligne.</p>"
        "<p>Ce recul n'est pas une politique délibérée&nbsp;: c'est le produit "
        "d'arbitrages séparés dont personne ne fait la somme.</p>",
        "",
        "opacite",
    )

    corps += cle(
        "5. L'exécutif reste maître des poursuites",
        "Les procureurs sont nommés par le garde des Sceaux. Une convention "
        "veut qu'il suive l'avis du Conseil supérieur de la magistrature — "
        "<b>rien ne l'y oblige en droit</b>. Le GRECO le relève depuis plus de "
        "dix ans, la réforme constitutionnelle a été abandonnée en 2019.",
        "<p>Le soupçon compte autant que le fait. Dans les affaires qui "
        "touchent au pouvoir, une justice dont on peut discuter "
        "l'indépendance organique ne produit pas de vérité acceptée&nbsp;: "
        "chaque décision est lue comme un acte politique, quelle qu'elle "
        "soit. C'est un coût pour tout le monde, y compris pour ceux qui sont "
        "relaxés.</p>"
        "<p>S'y ajoute le facteur temps. Une affaire financière complexe se "
        "compte en années d'instruction, parfois davantage&nbsp;; la "
        "prescription, les nullités de procédure et l'usure des dossiers font "
        "le reste. Une sanction qui arrive dix ans après les faits ne dissuade "
        "plus personne.</p>",
        "",
        "poursuites",
    )

    corps += cle(
        "6. Les moyens ne suivent pas le discours",
        "Entre le début des années 2010 et 2020, les effectifs du contrôle "
        "fiscal ont baissé d'environ un quart. Le plan de 2023 promet "
        "1&nbsp;500 agents d'ici 2027&nbsp;: <b>cela ne rattrape pas ce qui a "
        "été perdu</b>.",
        "<p>Le contraste est plus net encore sur le versant anticorruption. "
        "L'Agence française anticorruption compte de l'ordre de 50 agents pour "
        "contrôler les programmes de conformité de milliers d'entreprises et "
        "de collectivités. La Haute Autorité pour la transparence de la vie "
        "publique en compte une soixantaine pour ≈ 16&nbsp;000 déclarants. Le "
        "parquet national financier, une vingtaine de magistrats pour des "
        "centaines de procédures, souvent internationales.</p>"
        "<p>Ce n'est pas une question de budget global&nbsp;: les sommes en "
        "jeu sont dérisoires au regard des montants récupérés. C'est une "
        "question de priorité affichée.</p>",
        "",
        "moyens",
    )

    corps += cle(
        "7. Signaler une fraude reste un risque personnel",
        "La loi de 2022 est parmi les plus protectrices d'Europe. Mais elle "
        "protège contre les représailles&nbsp;; <b>elle ne compense rien</b>, "
        "et les procédures-bâillons continuent d'épuiser ceux qui parlent.",
        "<p>Le parcours type d'un lanceur d'alerte français reste le "
        "même&nbsp;: perte d'emploi, plusieurs années de procédure, frais "
        "d'avocat, et au mieux une reconnaissance tardive. L'aviseur fiscal "
        "rémunéré existe depuis 2017, mais son indemnisation est "
        "discrétionnaire, sans barème public, et son champ étroit.</p>"
        "<p>Les pays qui ont fait le choix inverse — une récompense "
        "proportionnelle aux sommes effectivement recouvrées — ont vu affluer "
        "des signalements exploitables. Le programme de la <i>Securities and "
        "Exchange Commission</i> américaine, qui verse de 10 à 30&nbsp;% des "
        "sanctions supérieures à un million de dollars, a distribué plus d'un "
        "milliard de dollars de primes, sur plusieurs milliards de sanctions "
        "<b>ordonnées</b> — ordonnées, et non encaissées&nbsp;: la distinction "
        "que nous demandons à l'État vaut aussi pour l'exemple dont nous nous "
        "réclamons.</p>",
        "",
        "alerte",
    )

    corps += vigilance(
        "<b>Ce diagnostic est une thèse, pas un constat neutre.</b> D'autres "
        "lectures existent, et elles ne sont pas absurdes&nbsp;: on peut "
        "soutenir que le dispositif progresse et qu'il lui faut du temps, ou "
        "que le vrai frein est budgétaire et non institutionnel. Nous "
        "pensons que la complexité et l'opacité sont premières, et que les "
        "moyens ne produisent leur effet qu'une fois ces deux-là traitées. "
        "C'est ce que la page <a href=\"programme.html\">Programme</a> "
        "propose de mettre à l'épreuve."
    )

    return page(
        "diagnostic.html",
        "Diagnostic — pourquoi la France plafonne contre la fraude",
        "Sept causes du plafonnement de la politique française contre la "
        "fraude et la corruption : complexité fiscale, niveau des "
        "prélèvements, recouvrement, opacité des données, indépendance des "
        "poursuites, moyens, statut du lanceur d'alerte.",
        corps,
    )


# ---------------------------------------------------------------------------
# 5. Programme — les dix mesures
# ---------------------------------------------------------------------------

def programme() -> str:
    corps = affiche(
        "La proposition libérale",
        "Dix mesures.<br>Aucune n'ajoute<br>"
        '<span class="cle-texte">une agence.</span>',
        "Trois blocs, dans l'ordre où ils doivent être menés&nbsp;: assécher "
        "la fraude en simplifiant la règle, l'exposer en publiant tout ce qui "
        "est public, la sanctionner en rendant les poursuites indépendantes et "
        "le recouvrement mesurable. Chaque mesure dit ce qu'elle remplace.",
    )

    corps += plan((
        ("assecher", "Assécher"),
        ("exposer", "Exposer"),
        ("sanctionner", "Sanctionner"),
        ("refus", "Ce que nous refusons"),
    ))

    corps += """
<h2 id="assecher" tabindex="-1">Bloc I — Assécher <span class="badge proposition">Proposition</span></h2>
<p>Une politique anti-fraude qui ne touche pas à la règle fiscale se condamne à
courir après ses propres exceptions. C'est le bloc le plus impopulaire des
trois, et c'est le plus déterminant.</p>
"""
    corps += mesures((
        ("Diviser par deux le nombre de dépenses fiscales en une législature",
         "<p>Chaque niche est réexaminée selon une règle unique&nbsp;: elle est "
         "supprimée si son efficacité n'est pas démontrée par une évaluation "
         "indépendante publiée. Le rendement dégagé est intégralement "
         "restitué en baisse de taux, et cette restitution est inscrite dans "
         "la loi organique qui porte la réforme&nbsp;: sans elle, la "
         "simplification devient une hausse d'impôt déguisée, et la mesure se "
         "retourne contre son objet.</p>"
         "<p>Une assiette large et un taux bas produisent mécaniquement moins "
         "de frontières à contourner, moins de contentieux, et moins de fraude "
         "involontaire.</p>",
         "près de 470 dépenses fiscales pour plus de 80&nbsp;Md&nbsp;€, "
         "recensées chaque année dans l'annexe « Voies et moyens » du budget, "
         "et dont une minorité seulement a fait l'objet d'une évaluation."),

        ("Un droit fiscal opposable : rescrit de droit sous trois mois",
         "<p>Toute personne, physique ou morale, peut demander à "
         "l'administration de se prononcer par écrit sur sa situation. "
         "Sans réponse dans les trois mois, la position du demandeur est "
         "réputée acceptée et lui est opposable. La doctrine administrative "
         "est publiée intégralement, en ligne, et l'administration ne peut "
         "s'en écarter rétroactivement.</p>"
         "<p>L'effet attendu n'est pas seulement de confort&nbsp;: il sépare "
         "enfin le fraudeur de celui qui n'avait pas compris, et permet de "
         "concentrer le contrôle sur le premier.</p>",
         "le rescrit existe mais reste lent, partiel et peu utilisé&nbsp;; "
         "l'incertitude sur l'interprétation est la première cause de "
         "contentieux fiscal."),

        ("Verser les prestations à la source, sur les données déjà détenues",
         "<p>Les revenus sont déjà connus de l'administration mois par mois, "
         "par la déclaration sociale nominative. Les prestations sous "
         "condition de ressources doivent être calculées et versées à partir "
         "de ces données, sans déclaration de l'allocataire.</p>"
         "<p>Ce qui disparaît alors n'est pas seulement la fraude "
         "déclarative&nbsp;: c'est aussi l'indu de bonne foi, et une grande "
         "partie du non-recours. Trois problèmes, une seule cause.</p>",
         "l'allocataire déclare lui-même ses ressources, plusieurs fois par "
         "an&nbsp;; la DREES estime qu'environ un tiers des éligibles au RSA "
         "ne le demandent pas, pendant que les caisses poursuivent des indus "
         "qu'elles ont elles-mêmes provoqués."),
    ))

    corps += """
<h2 id="exposer" tabindex="-1">Bloc II — Exposer <span class="badge proposition">Proposition</span></h2>
<p>Ce qui est financé par l'impôt appartient à ceux qui le paient. La
publication n'est pas une faveur faite aux curieux&nbsp;: c'est le seul contrôle
qui passe à l'échelle, parce qu'il mobilise des milliers de regards au lieu de
cinquante agents.</p>
"""
    corps += mesures((
        ("Publier 100 % de la dépense publique en données ouvertes",
         "<p>Marchés, subventions, aides aux entreprises, dépenses de l'État "
         "et des collectivités&nbsp;: chaque engagement est publié dans les "
         "trente jours, en format ouvert et lisible par une machine, sur un "
         "portail unique. Les marchés suivent le standard international "
         "<i>Open Contracting Data Standard</i>, avenants et sous-traitants "
         "compris. Le non-respect prive l'acte de force exécutoire.</p>"
         "<p>Le précédent ukrainien — <i>Prozorro</i>, et son outil de "
         "signalement citoyen <i>DoZorro</i> — montre qu'une plateforme "
         "ouverte change le comportement des acheteurs avant même qu'un "
         "contrôle ait lieu.</p>",
         "les données existent mais sont dispersées entre des centaines de "
         "profils d'acheteurs, publiées avec retard, dans des formats "
         "hétérogènes, et souvent sans les avenants."),

        ("Rouvrir le registre des bénéficiaires effectifs",
         "<p>Accès de plein droit, gratuit et traçable, pour les journalistes, "
         "les chercheurs, les ONG et les entreprises soumises à des "
         "obligations de vigilance — exactement le cadre que la Cour de "
         "justice de l'Union européenne a jugé proportionné, et que le paquet "
         "anti-blanchiment européen de 2024 organise. La France le transpose "
         "au maximum de ce que le droit permet, et non au minimum.</p>",
         "l'accès du grand public est restreint depuis l'arrêt de la CJUE de "
         "novembre&nbsp;2022&nbsp;; l'outil qui avait permis l'essentiel des "
         "révélations de la décennie est devenu difficile d'accès."),

        ("Publier chaque année un chiffrage officiel de la fraude",
         "<p>Un <i>écart fiscal et social</i> à la française&nbsp;: une "
         "estimation annuelle de la différence entre ce qui est dû et ce qui "
         "est perçu, produite par l'Insee avec le Conseil des prélèvements "
         "obligatoires, selon une méthode publiée et critiquable, révisable "
         "d'une année sur l'autre, et débattue au Parlement avant le vote du "
         "budget.</p>"
         "<p>C'est la mesure qui rend toutes les autres évaluables. Sans "
         "dénominateur, « un milliard récupéré » ne veut rien dire.</p>",
         "aucune estimation officielle consolidée n'existe&nbsp;; le "
         "Royaume-Uni publie la sienne depuis 2005, l'Italie, la Suède et les "
         "États-Unis également."),
    ))

    corps += """
<h2 id="sanctionner" tabindex="-1">Bloc III — Sanctionner <span class="badge proposition">Proposition</span></h2>
<p>Une sanction n'existe que si elle est probable, rapide et encaissée. Les
trois conditions manquent aujourd'hui, et aucune ne se règle par une
circulaire.</p>
"""
    corps += mesures((
        ("Rendre les poursuites indépendantes de l'exécutif",
         "<p>Inscrire dans la Constitution l'avis conforme du Conseil "
         "supérieur de la magistrature pour la nomination et la discipline des "
         "magistrats du parquet. C'est la réforme réclamée par le GRECO depuis "
         "plus de dix ans, votée en termes identiques par les deux assemblées "
         "puis abandonnée avant le Congrès en 2019.</p>"
         "<p>S'y ajoute un objectif de délai&nbsp;: une procédure financière "
         "qui dure plus de cinq ans fait l'objet d'un rapport public du "
         "ministère public expliquant pourquoi.</p>",
         "le garde des Sceaux nomme les procureurs&nbsp;; il suit l'avis du "
         "CSM par convention, sans y être tenu en droit."),

        ("Une prime au lanceur d'alerte, jusqu'à 30 % des sommes recouvrées",
         "<p>Barème public et progressif, versé uniquement sur les sommes "
         "<b>effectivement encaissées</b>, plafonné, ouvert à la fraude "
         "fiscale, sociale et aux atteintes à la probité dans la commande "
         "publique. La décision appartient à une autorité indépendante, pas à "
         "l'administration bénéficiaire.</p>"
         "<p>En regard, une protection réelle&nbsp;: prise en charge des frais "
         "de procédure dès la recevabilité du signalement, et sanction "
         "financière dissuasive des représailles et des procédures-bâillons.</p>",
         "l'aviseur fiscal rémunéré existe depuis 2017, mais son indemnisation "
         "est discrétionnaire, sans barème public, et d'un champ étroit."),

        ("Exclure des marchés publics ceux qui ont corrompu",
         "<p>Toute personne morale condamnée pour atteinte à la probité, ou "
         "ayant conclu une convention judiciaire d'intérêt public, est exclue "
         "de la commande publique pour une durée proportionnée, inscrite dans "
         "un registre public tenu par l'AFA. L'exclusion peut être levée par "
         "décision motivée et publiée si l'entreprise démontre avoir remédié "
         "aux défaillances — le mécanisme existe déjà en droit européen.</p>"
         "<p>La CJIP reste&nbsp;: c'est un bon outil. Mais une amende que "
         "l'entreprise provisionne ne change pas un modèle d'affaires&nbsp;; "
         "la perte de l'accès aux marchés, si.</p>",
         "la CJIP éteint les poursuites sans reconnaissance de culpabilité et "
         "n'emporte aucune exclusion automatique&nbsp;; l'entreprise "
         "sanctionnée peut soumissionner le lendemain."),

        ("Mesurer le recouvrement, pas les annonces",
         "<p>Publication trimestrielle, service par service, du montant "
         "notifié, du montant encaissé et du délai moyen&nbsp;; les objectifs "
         "des administrations et l'intéressement de leurs directions portent "
         "sur l'encaissement. Généralisation des saisies conservatoires dès "
         "l'engagement du contrôle, et extension du périmètre de l'AGRASC à la "
         "fraude fiscale et sociale organisée.</p>",
         "l'indicateur public est le montant notifié&nbsp;; le tiers jamais "
         "encaissé n'apparaît dans aucune série détaillée."),
    ))

    corps += cle(
        "Ce que nous refusons",
        "Un programme libéral contre la fraude ne peut pas être un programme "
        "de surveillance. Quatre lignes que nous ne franchirons pas — et il "
        "faut les écrire avant qu'on nous les prête.",
        "<p><b>Le fichage généralisé des allocataires.</b> Croiser des "
        "fichiers pour verser un droit à la source est une chose&nbsp;; "
        "constituer un profil de risque sur des millions de personnes en est "
        "une autre. Tout croisement doit avoir une finalité définie par la "
        "loi, une durée de conservation, et un contrôle de la CNIL.</p>"
        "<p><b>L'algorithme opaque.</b> Un score de suspicion qui déclenche un "
        "contrôle doit être publié dans ses critères, contestable, et faire "
        "l'objet d'une intervention humaine avant toute décision "
        "défavorable.</p>"
        "<p><b>La présomption de culpabilité.</b> L'indu n'est pas la fraude. "
        "Confondre les deux, c'est traiter en délinquant quelqu'un qui n'a pas "
        "compris un formulaire — et c'est exactement ce que la mesure n°&nbsp;3 "
        "vise à faire disparaître.</p>"
        "<p><b>La transparence à sens unique.</b> Nous demandons la "
        "publication de ce qui est <b>public</b> — contrats, subventions, "
        "intérêts des décideurs, bénéficiaires effectifs des sociétés. Pas des "
        "données personnelles des citoyens ordinaires.</p>",
        "",
        "refus",
    )

    corps += """
<div class="creme">
  <p class="surtitre">Et ensuite</p>
  <h2 class="serif" style="text-transform:none">Ce que cela coûte, et ce que cela peut rapporter</h2>
  <p>Nous ne promettons pas de « récupérer 100&nbsp;milliards ». La page
  suivante donne, mesure par mesure, un ordre de grandeur du coût, du rendement
  possible, et surtout <b>notre degré de confiance</b> dans chaque ligne — y
  compris quand il est faible.</p>
  <p class="actions"><a class="bouton" href="chiffrage.html">Voir le chiffrage</a></p>
</div>
"""

    return page(
        "programme.html",
        "Programme — dix mesures libérales contre la fraude et la corruption",
        "Dix mesures : simplification fiscale, prestations à la source, "
        "publication intégrale de la dépense publique, réouverture du registre "
        "des bénéficiaires effectifs, chiffrage annuel de la fraude, "
        "indépendance du parquet, prime au lanceur d'alerte, exclusion des "
        "marchés publics.",
        corps,
    )


# ---------------------------------------------------------------------------
# 6. Chiffrage — ce que cela coûte, ce que cela peut rapporter
# ---------------------------------------------------------------------------

def chiffrage() -> str:
    corps = affiche(
        "Le chiffrage",
        "Nous ne promettons pas<br>"
        '<span class="cle-texte">cent milliards.</span>',
        "Un programme qui annonce un rendement précis sur une assiette que "
        "personne ne sait mesurer ment deux fois. Voici ce que nous pouvons "
        "dire honnêtement&nbsp;: le coût de chaque mesure, l'ordre de grandeur "
        "de ce qu'elle peut rendre, et notre degré de confiance — y compris "
        "quand il est faible.",
    )

    corps += plan((
        ("methode", "La méthode"),
        ("cout", "Le coût"),
        ("rendement", "Le rendement"),
        ("limites", "Les limites"),
    ))

    corps += '<h2 id="methode" tabindex="-1">Comment nous chiffrons</h2>'
    corps += """
<p>Trois règles, et elles sont restrictives à dessein&nbsp;:</p>
"""
    corps += gestes((
        "<strong>Le coût est chiffré, le rendement est encadré.</strong> Un "
        "portail de données ou 1&nbsp;500 agents se chiffrent au budget près. "
        "Ce qu'une mesure fera rentrer dépend de comportements qui changent "
        "— nous donnons une fourchette, jamais un point.",
        "<strong>Rien n'est compté deux fois.</strong> Simplifier la règle et "
        "renforcer le contrôle agissent sur la même assiette&nbsp;: additionner "
        "leurs rendements supposés serait la première tricherie d'un programme "
        "qui parle de fraude.",
        "<strong>Le degré de confiance est affiché.</strong> Quand nous ne "
        "savons pas, la colonne le dit, et la ligne ne se somme pas avec les "
        "autres.",
    ))

    corps += '<h2 id="cout" tabindex="-1">Ce que cela coûte</h2>'
    corps += """
<p>Le coût budgétaire direct du programme est faible&nbsp;: l'essentiel des
mesures est institutionnel ou normatif. Les deux seuls postes lourds sont les
effectifs et la refonte des systèmes d'information.</p>
"""
    corps += tableau(
        "Coût annuel en régime de croisière (ordres de grandeur, euros de 2026)",
        ("Poste", "Nature", "Coût annuel", "Confiance"),
        (
            ("Portail unique de la dépense publique",
             "Construction puis exploitation&nbsp;; réutilise des briques "
             "existantes (Chorus, data.gouv.fr, profils d'acheteurs)",
             "20 à 50 M&nbsp;€", "Bonne"),
            ("Versement des prestations à la source",
             "Refonte des systèmes d'information des caisses&nbsp;; comparable "
             "au prélèvement à la source de 2019. 150 à 400&nbsp;M&nbsp;€ au "
             "total, amortis sur cinq ans",
             "30 à 80 M&nbsp;€", "Moyenne"),
            ("Renforcement des effectifs de contrôle et de poursuite",
             "≈ 2&nbsp;000 équivalents temps plein supplémentaires (contrôle "
             "fiscal, AFA, HATVP, PNF, juridictions financières), <b>en sus</b> "
             "des 1&nbsp;500 agents du plan de 2023&nbsp;; au coût complet "
             "employeur de 80 à 110&nbsp;k&nbsp;€ par agent, rémunération "
             "chargée, support et immobilier compris",
             "160 à 220 M&nbsp;€", "Bonne"),
            ("Chiffrage annuel de l'écart fiscal et social",
             "Une équipe permanente à l'Insee, enquêtes de contrôle aléatoire",
             "5 à 15 M&nbsp;€", "Bonne"),
            ("Prime au lanceur d'alerte",
             "Versée sur les sommes <b>effectivement encaissées</b>&nbsp;: le "
             "poste ne coûte que s'il rapporte",
             "Autofinancé par construction", "Bonne"),
            ("<b>Total</b>",
             "Somme des lignes ci-dessus, refonte des systèmes d'information "
             "amortie sur cinq ans",
             "<b>≈ 215 à 365 M&nbsp;€/an</b>", "—"),
        ),
        ("texte", "long", "nombre", "texte"),
    )
    corps += """
<p class="discret">À comparer aux ≈&nbsp;10,6&nbsp;Md&nbsp;€ que le seul
contrôle fiscal a <b>effectivement encaissés</b> en 2023 — et non aux
≈&nbsp;15&nbsp;Md&nbsp;€ notifiés, car la distinction que nous demandons à
l'État vaut d'abord pour nous&nbsp;: le coût du programme représente de l'ordre
de 2 à 3,5&nbsp;% de ce montant.</p>
"""

    corps += '<h2 id="rendement" tabindex="-1">Ce que cela peut rapporter</h2>'
    corps += """
<p>Ici, la prudence est de règle. Les fourchettes ci-dessous ne sont pas des
prévisions&nbsp;: ce sont des ordres de grandeur construits à partir de ce qui a
été observé ailleurs, et ils supposent une mise en œuvre complète sur une
législature.</p>
"""
    corps += tableau(
        "Rendement annuel possible en régime de croisière (ordres de grandeur)",
        ("Mesure", "Canal de l'effet", "Rendement", "Confiance"),
        (
            ("Prestations versées à la source",
             "Disparition de l'essentiel de la fraude déclarative et des indus "
             "de bonne foi&nbsp;; hausse mécanique des versements liée à la "
             "baisse du non-recours",
             "Effet net incertain&nbsp;: gain en fraude, coût en non-recours "
             "résorbé", "Faible"),
            ("Publication intégrale de la commande publique",
             "Baisse des prix d'attribution et de la surfacturation&nbsp;; "
             "effet dissuasif avant contrôle. Une baisse de 1&nbsp;% sur "
             "≈ 160&nbsp;Md&nbsp;€ vaut 1,6&nbsp;Md&nbsp;€",
             "0,5 à 3 Md&nbsp;€", "Moyenne"),
            ("Recouvrement effectif renforcé",
             "Ramener <b>durablement</b> la part encaissée de ≈ 70&nbsp;% "
             "(2023) à ≈ 80&nbsp;% des montants notifiés — un niveau déjà "
             "atteint en 2019 et en 2021, ce qui rend le gain plausible mais "
             "interdit de le présenter comme acquis",
             "1 à 1,5 Md&nbsp;€", "Moyenne"),
            ("Prime au lanceur d'alerte",
             "Signalements exploitables sur des montages que le contrôle de "
             "routine ne voit pas",
             "0,2 à 1 Md&nbsp;€", "Faible"),
            ("Réduction des dépenses fiscales",
             "Ce n'est pas un rendement anti-fraude mais une recette "
             "budgétaire — et nous proposons de la restituer intégralement en "
             "baisse de taux",
             "Neutre par construction", "—"),
            ("Chiffrage annuel de l'écart fiscal",
             "Aucun rendement direct&nbsp;: c'est la mesure qui rend les "
             "autres évaluables",
             "Nul par nature", "—"),
            ("<b>Ordre de grandeur agrégé</b>",
             "Somme des trois lignes chiffrables, hors effets non chiffrables "
             "et sans double compte",
             "<b>≈ 1,7 à 5,5 Md&nbsp;€/an</b>", "Moyenne"),
        ),
        ("texte", "long", "nombre", "texte"),
    )

    corps += cle(
        "Pourquoi un ordre de grandeur, et pas un chiffre",
        "Parce que le dénominateur manque. Tant qu'aucune institution ne "
        "publie l'écart entre ce qui est dû et ce qui est perçu, <b>toute "
        "promesse de rendement est un pari présenté comme un calcul</b>.",
        "<p>Les chiffres qui circulent dans le débat public — « 80 milliards », "
        "« 100 milliards » — sont des estimations d'<i>assiette</i>, pas de "
        "<i>rendement</i>. Même une politique parfaite ne récupère pas "
        "l'intégralité d'une assiette&nbsp;: une partie des montants est "
        "insolvable, une autre disparaît avec l'activité qui la portait, une "
        "troisième n'aurait jamais existé sous un régime différent.</p>"
        "<p>C'est pourquoi la mesure n°&nbsp;6 du programme — le chiffrage "
        "annuel — n'est pas une mesure technique parmi d'autres&nbsp;: c'est la "
        "condition pour que le débat cesse d'être une enchère.</p>",
        "",
        "limites",
    )

    corps += vigilance(
        "<b>Ce chiffrage n'a aucune valeur officielle.</b> Il n'émane ni de "
        "Bercy, ni de la Cour des comptes, ni d'un institut indépendant. Il "
        "est construit à partir de sources publiques, avec des hypothèses que "
        "nous indiquons et qui peuvent être contestées — et nous préférons une "
        "fourchette large assumée à un chiffre rond invérifiable. Le détail "
        "des hypothèses et les sources sont sur la page "
        "<a href=\"sources.html\">Sources</a>&nbsp;; une erreur se signale sur "
        "le dépôt, et se corrige."
    )

    return page(
        "chiffrage.html",
        "Chiffrage — ce que coûte et ce que peut rapporter le programme",
        "Le coût annuel et le rendement possible de chacune des dix mesures, "
        "avec le degré de confiance associé — et les raisons pour lesquelles "
        "nous refusons d'annoncer un chiffre unique.",
        corps,
    )


# ---------------------------------------------------------------------------
# 7. Sources — tout ce qui est cité, avec le lien et la date
# ---------------------------------------------------------------------------

def _lien(libelle: str, adresse: str) -> str:
    return f'<a href="{adresse}">{libelle}</a>'


def sources() -> str:
    corps = affiche(
        "La confiance",
        "Tout ce qui est écrit<br>"
        '<span class="cle-texte">est vérifiable</span>',
        "Aucun chiffre de ce site ne vient de nous. Chacun a une source, une "
        "date et un périmètre, et ils sont listés ici. Quand une publication "
        "n'a pas d'adresse stable, nous donnons sa référence complète et le "
        "lien vers l'institution qui la publie.",
    )

    corps += """
<div class="note resume">
  <p>Trois précautions de lecture, qui valent pour tout le site&nbsp;:</p>
  <p>— une <b>estimation</b> n'est pas une mesure&nbsp;: elle dépend d'une
  méthode, et deux méthodes honnêtes donnent deux résultats&nbsp;;<br>
  — un montant <b>détecté</b> n'est pas un montant <b>commis</b>&nbsp;: mieux
  détecter fait monter les chiffres sans que rien ait changé&nbsp;;<br>
  — un montant <b>notifié</b> n'est pas un montant <b>encaissé</b>.</p>
  <p class="discret">Liens vérifiés en septembre&nbsp;2026.</p>
</div>
"""

    corps += '<h2 id="fiscal" tabindex="-1">Fraude fiscale et contrôle</h2>'
    corps += tableau(
        "Sources — fraude fiscale, contrôle et recouvrement",
        ("Source", "Ce qu'elle établit", "Où la trouver"),
        (
            ("Conseil des prélèvements obligatoires",
             "Rapports sur la fraude aux prélèvements obligatoires&nbsp;; "
             "estimation de 2007 et travaux ultérieurs sur la mesure de la "
             "fraude.",
             _lien("ccomptes.fr — CPO",
                   "https://www.ccomptes.fr/fr/conseil-des-prelevements-obligatoires")),
            ("Cour des comptes",
             "Rapports annuels et thématiques&nbsp;; constat de l'absence "
             "d'estimation fiable et récente de la fraude fiscale.",
             _lien("ccomptes.fr", "https://www.ccomptes.fr/")),
            ("DGFiP",
             "Résultats annuels du contrôle fiscal&nbsp;: montants notifiés, "
             "montants encaissés, nombre de contrôles.",
             _lien("economie.gouv.fr — DGFiP",
                   "https://www.economie.gouv.fr/dgfip")),
            ("Insee",
             "Travaux d'estimation de la fraude à la TVA (publication de "
             "2022 portant sur l'année 2012).",
             _lien("insee.fr", "https://www.insee.fr/")),
            ("Commission européenne",
             "Rapports annuels <i>VAT Gap</i>&nbsp;: écart entre la TVA "
             "théorique et la TVA perçue, par État membre. Attention, le "
             "périmètre inclut les erreurs et les défaillances, pas seulement "
             "la fraude.",
             _lien("taxation-customs.ec.europa.eu",
                   "https://taxation-customs.ec.europa.eu/taxation/vat/vat-gap_en")),
            ("Solidaires Finances Publiques",
             "Estimation syndicale de 80 à 100&nbsp;Md&nbsp;€ (2019), la plus "
             "citée dans le débat public et jamais reprise par l'État.",
             _lien("solidairesfinancespubliques.org",
                   "https://solidairesfinancespubliques.org/")),
            ("HM Revenue &amp; Customs (Royaume-Uni)",
             "<i>Measuring tax gaps</i>&nbsp;: la série annuelle de référence, "
             "publiée depuis 2005. C'est le modèle de notre mesure n°&nbsp;6.",
             _lien("gov.uk — Measuring tax gaps",
                   "https://www.gov.uk/government/statistics/measuring-tax-gaps")),
        ),
        ("texte", "long", "texte"),
    )

    corps += '<h2 id="social" tabindex="-1">Fraude sociale et prestations</h2>'
    corps += tableau(
        "Sources — cotisations, prestations, non-recours",
        ("Source", "Ce qu'elle établit", "Où la trouver"),
        (
            ("Haut Conseil du financement de la protection sociale",
             "Estimation de la fraude aux cotisations sociales&nbsp;: 6,8 à "
             "8,4&nbsp;Md&nbsp;€ par an (rapport de 2022).",
             _lien("securite-sociale.fr", "https://www.securite-sociale.fr/")),
            ("URSSAF Caisse nationale",
             "Résultats annuels de la lutte contre le travail "
             "dissimulé&nbsp;: montants redressés.",
             _lien("urssaf.org", "https://www.urssaf.org/")),
            ("CNAF, CNAM, CNAV, MSA",
             "Rapports annuels&nbsp;: préjudice estimé et fraude détectée, "
             "branche par branche.",
             _lien("securite-sociale.fr", "https://www.securite-sociale.fr/")),
            ("Cour des comptes",
             "Rapports sur la lutte contre les fraudes aux prestations "
             "sociales et sur la fiabilité des données des caisses.",
             _lien("ccomptes.fr", "https://www.ccomptes.fr/")),
            ("DREES",
             "Travaux sur le non-recours aux prestations&nbsp;: environ un "
             "tiers des éligibles au RSA ne le demandent pas (étude de 2022).",
             _lien("drees.solidarites-sante.gouv.fr",
                   "https://drees.solidarites-sante.gouv.fr/")),
        ),
        ("texte", "long", "texte"),
    )

    corps += '<h2 id="corruption" tabindex="-1">Corruption et probité</h2>'
    corps += tableau(
        "Sources — corruption, transparence, poursuites",
        ("Source", "Ce qu'elle établit", "Où la trouver"),
        (
            ("Transparency International",
             "Indice de perception de la corruption&nbsp;: note et rang de la "
             "France, millésimes 2019 à 2024. Mesure une perception, pas un "
             "nombre d'actes.",
             _lien("transparency.org — CPI 2024",
                   "https://www.transparency.org/en/cpi/2024")),
            ("GRECO — Conseil de l'Europe",
             "Rapports d'évaluation et de conformité sur la France, "
             "notamment le cinquième cycle (hautes fonctions de l'exécutif et "
             "services répressifs).",
             _lien("coe.int — GRECO", "https://www.coe.int/fr/web/greco")),
            ("Agence française anticorruption",
             "Rapports annuels, recommandations, données sur les "
             "condamnations pour atteintes à la probité, suivi des CJIP.",
             _lien("agence-francaise-anticorruption.gouv.fr",
                   "https://www.agence-francaise-anticorruption.gouv.fr/")),
            ("Haute Autorité pour la transparence de la vie publique",
             "Déclarations d'intérêts et de patrimoine, répertoire des "
             "représentants d'intérêts, avis de déontologie.",
             _lien("hatvp.fr", "https://www.hatvp.fr/")),
            ("TRACFIN",
             "Rapport annuel d'activité&nbsp;: volume de déclarations de "
             "soupçon reçues, notes transmises.",
             _lien("economie.gouv.fr — TRACFIN",
                   "https://www.economie.gouv.fr/tracfin")),
            ("Parquet européen",
             "Rapport annuel&nbsp;: enquêtes ouvertes en France sur les "
             "atteintes au budget de l'Union.",
             _lien("eppo.europa.eu", "https://www.eppo.europa.eu/fr")),
            ("Cour de justice de l'Union européenne",
             "Arrêt du 22&nbsp;novembre 2022, affaires jointes "
             "C-37/20 et C-601/20&nbsp;: l'accès du grand public au registre "
             "des bénéficiaires effectifs est invalidé.",
             _lien("curia.europa.eu", "https://curia.europa.eu/")),
        ),
        ("texte", "long", "texte"),
    )

    corps += '<h2 id="marches" tabindex="-1">Commande publique et dépense</h2>'
    corps += tableau(
        "Sources — marchés publics, dépense publique, données ouvertes",
        ("Source", "Ce qu'elle établit", "Où la trouver"),
        (
            ("Observatoire économique de la commande publique",
             "Recensement annuel des marchés publics&nbsp;: montants, nombre "
             "de contrats, répartition par acheteur.",
             _lien("economie.gouv.fr — DAJ",
                   "https://www.economie.gouv.fr/daj")),
            ("Insee",
             "Comptes nationaux&nbsp;: dépense publique, prélèvements "
             "obligatoires, PIB.",
             _lien("insee.fr", "https://www.insee.fr/")),
            ("Eurostat",
             "Comparaison européenne du taux de prélèvements obligatoires.",
             _lien("ec.europa.eu/eurostat", "https://ec.europa.eu/eurostat")),
            ("data.gouv.fr",
             "Jeux de données publics existants&nbsp;: marchés, subventions, "
             "comptes des collectivités. Point de départ de notre mesure "
             "n°&nbsp;4.",
             _lien("data.gouv.fr", "https://www.data.gouv.fr/")),
            ("<i>Open Contracting Data Standard</i>",
             "Le standard international de publication des marchés publics "
             "que nous proposons d'adopter.",
             _lien("standard.open-contracting.org",
                   "https://standard.open-contracting.org/")),
            ("Prozorro (Ukraine)",
             "Plateforme ouverte de la commande publique&nbsp;; référence "
             "internationale en matière de publication intégrale.",
             _lien("prozorro.gov.ua", "https://prozorro.gov.ua/en")),
            ("USAspending (États-Unis)",
             "Publication en ligne de la totalité de la dépense fédérale, "
             "contrat par contrat.",
             _lien("usaspending.gov", "https://www.usaspending.gov/")),
        ),
        ("texte", "long", "texte"),
    )

    corps += '<h2 id="textes" tabindex="-1">Textes et travaux cités</h2>'
    corps += tableau(
        "Références complètes des textes et travaux mentionnés",
        ("Référence", "Objet"),
        (
            ("LOI n°&nbsp;93-122 du 29 janvier 1993 (Sapin&nbsp;I)",
             "Prévention de la corruption, transparence de la vie économique "
             "et des procédures publiques."),
            ("LOI n°&nbsp;2013-907 du 11 octobre 2013",
             "Transparence de la vie publique&nbsp;; création de la HATVP."),
            ("LOI n°&nbsp;2013-1117 du 6 décembre 2013",
             "Lutte contre la fraude fiscale et la grande délinquance "
             "économique et financière&nbsp;; création du PNF."),
            ("LOI n°&nbsp;2016-1691 du 9 décembre 2016 (Sapin&nbsp;II)",
             "Transparence, lutte contre la corruption et modernisation de la "
             "vie économique&nbsp;; AFA, CJIP, répertoire des représentants "
             "d'intérêts, statut du lanceur d'alerte."),
            ("LOI n°&nbsp;2018-898 du 23 octobre 2018",
             "Lutte contre la fraude&nbsp;; police fiscale, publication des "
             "sanctions, aviseur fiscal."),
            ("Directive (UE) 2019/1937 du 23 octobre 2019",
             "Protection des personnes qui signalent des violations du droit "
             "de l'Union."),
            ("LOI n°&nbsp;2022-401 du 21 mars 2022 (Waserman)",
             "Amélioration de la protection des lanceurs d'alerte&nbsp;; "
             "transposition de la directive de 2019."),
            ("Plan gouvernemental de lutte contre toutes les fraudes aux "
             "finances publiques, mai 2023",
             "1&nbsp;500 agents supplémentaires au contrôle fiscal d'ici 2027, "
             "renforcement des contrôles sur les hauts patrimoines."),
            ("Allingham M. et Sandmo A., <i>Income tax evasion: a theoretical "
             "analysis</i>, Journal of Public Economics, 1972",
             "Le modèle économique de référence de la décision de "
             "fraude&nbsp;: gain attendu, probabilité de détection, sanction."),
            ("<i>SEC Whistleblower Program</i> (États-Unis, depuis 2011)",
             "Récompense de 10 à 30&nbsp;% des sanctions supérieures à un "
             "million de dollars&nbsp;; modèle de notre mesure n°&nbsp;8. Voir "
             + _lien("sec.gov/whistleblower",
                     "https://www.sec.gov/whistleblower") + "."),
        ),
        ("long", "long"),
    )

    corps += """
<p class="discret">Les textes français sont consultables sur
<a href="https://www.legifrance.gouv.fr/">Légifrance</a>, les textes européens
sur <a href="https://eur-lex.europa.eu/">EUR-Lex</a>&nbsp;: la référence
complète donnée ci-dessus suffit à les y retrouver.</p>
"""

    corps += vigilance(
        "<b>Une erreur se signale, et se corrige.</b> Si un chiffre de ce site "
        "vous paraît faux, obsolète ou sorti de son contexte, ouvrez un "
        "signalement sur le dépôt&nbsp;: il sera corrigé, et la correction "
        "sera visible dans l'historique. C'est le minimum que puisse offrir un "
        "site qui réclame la traçabilité de l'argent public."
    )

    return page(
        "sources.html",
        "Sources — d'où viennent les chiffres de ce site",
        "Toutes les sources citées sur ce site : administrations, juridictions "
        "financières, organisations internationales, textes de loi — avec leur "
        "date, leur périmètre et le lien pour les vérifier.",
        corps,
    )
