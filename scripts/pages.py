"""Le contenu des huit pages.

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
        "La France prélève au deuxième rang de l'Union européenne, derrière "
        "le Danemark, et dépense 1&nbsp;714&nbsp;milliards d'euros par an — "
        "sans publier le moindre chiffrage officiel de ce qui lui échappe. Notre programme "
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
    <a class="bouton" href="programme.html">Lire les douze mesures</a>
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
         "de 6 à 100&nbsp;milliards d'euros selon le périmètre retenu."),
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
         "La commande publique pèse 233&nbsp;milliards d'euros recensés en "
         "2024, près de 8&nbsp;% du PIB, dont 101 pour les seules "
         "collectivités. C'est le premier lieu de la corruption ordinaire, et "
         "le relèvement répété des seuils de gré à gré l'a rendu moins "
         "visible, pas plus honnête."),
    ))

    corps += "<h2>Notre méthode&nbsp;: trois gestes, dans cet ordre</h2>"
    corps += gestes((
        "<strong>Assécher.</strong> Une règle illisible est une règle qu'on "
        "contourne, et 465 dépenses fiscales font une règle illisible. "
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
  <h2 class="serif" style="text-transform:none">Sept pages, et l'on a fait le tour</h2>
  <p><a href="constat.html"><b>Constat</b></a> — ce que l'on sait et ce que
  l'on ne sait pas de la fraude et de la corruption en France, chiffre par
  chiffre.<br>
  <a href="dispositif.html"><b>Dispositif</b></a> — la politique actuelle&nbsp;:
  trente ans de textes, quatorze institutions, ce qu'elles font et ce
  qu'elles obtiennent.<br>
  <a href="diagnostic.html"><b>Diagnostic</b></a> — pourquoi ce dispositif
  plafonne, en sept causes.<br>
  <a href="programme.html"><b>Programme</b></a> — les douze mesures, et ce
  que chacune remplace.<br>
  <a href="chiffrage.html"><b>Chiffrage</b></a> — ce que cela coûte, ce que
  cela peut rapporter, et notre degré de confiance dans chaque ligne.<br>
  <a href="objections.html"><b>Objections</b></a> — les neuf critiques les plus
  solides qui nous sont faites, et nos réponses, dont quatre qui concèdent.<br>
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
        "statistique, d'une commission ou d'une caisse — et vont de 6 à "
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
        ("Ce qui échapperait au fisc", "6 à 100 Md €",
         "L'écart entre la plus basse et la plus haute des estimations "
         "publiques. En décembre&nbsp;2025, la Cour des comptes refuse "
         "toujours d'arbitrer entre elles."),
        ("Ce que le contrôle fiscal notifie", "17,1 Md €",
         "En 2025, droits et pénalités&nbsp;; 11,4&nbsp;Md&nbsp;€ encaissés, "
         "soit ≈ 67&nbsp;% — contre 80&nbsp;% en 2021 (DGFiP)."),
        ("Cotisations sociales éludées", "6 à 7,8 Md €",
         "Par an, travail dissimulé des salariés du privé non agricole "
         "(HCFiPS, décembre&nbsp;2024)."),
        ("Perception de la corruption", "66 / 100",
         "Note de la France en 2025, 27ᵉ sur 182&nbsp;; elle était de 72/100 "
         "en 2022 (Transparency International)."),
    ))

    corps += cle(
        "Combien coûte la fraude fiscale ?",
        "Sept sources publiques, six chiffres, un refus de chiffrer — et "
        "aucun arbitrage de l'État. "
        "L'écart n'est pas seulement statistique&nbsp;: les <b>périmètres</b> "
        "diffèrent, et personne n'est chargé de les réconcilier.",
        tableau(
            "Estimations publiques de la fraude fiscale en France",
            ("Source", "Millésime", "Périmètre", "Estimation"),
            (
                ("Solidaires Finances Publiques", "2019", "Fraude fiscale, tous impôts",
                 "80 à 100 Md&nbsp;€/an"),
                ("G. Zucman, repris par la Cour des comptes", "2025",
                 "Fraude fiscale", "70 à 80 Md&nbsp;€/an"),
                ("Conseil des prélèvements obligatoires", "2007",
                 "Fraude aux prélèvements obligatoires", "29 à 40 Md&nbsp;€/an"),
                ("Insee", "2022 (année 2012)", "TVA seule", "20 à 26 Md&nbsp;€"),
                ("Commission européenne, <i>VAT&nbsp;Gap</i>", "2023 (année 2021)",
                 "TVA seule, fraude <b>et</b> erreurs et défaillances",
                 "≈ 9,6 Md&nbsp;€, soit 4,9&nbsp;% des recettes théoriques"),
                ("DGFiP, travaux préliminaires", "2024",
                 "TVA <b>déclarée</b> seule", "6 à 10 Md&nbsp;€"),
                ("<b>Cour des comptes</b>", "décembre&nbsp;2025",
                 "Fraude fiscale",
                 "<b>Aucun chiffrage.</b> La Cour refuse d'arbitrer entre les "
                 "estimations en circulation et recommande de mesurer l'écart "
                 "fiscal, ce qu'une trentaine d'administrations de l'OCDE font "
                 "déjà"),
            ),
            ("texte", "date", "long", "long"),
        ),
        "Les périmètres ne se recouvrent pas et les millésimes s'échelonnent "
        "sur dix-huit ans&nbsp;: ce tableau ne dit pas laquelle de ces "
        "estimations est juste, il dit qu'aucune institution n'est chargée de "
        "le trancher — et que la Cour des comptes le constatait encore en "
        "décembre&nbsp;2025. Voir "
        "<a href=\"sources.html#fiscal\">Sources</a>.",
        "fiscale",
    )

    corps += cle(
        "Le contrôle fiscal rapporte-t-il ?",
        "Il notifie 17,1&nbsp;milliards d'euros en 2025 et en encaisse 11,4. "
        "L'écart d'un tiers est structurel — et <b>il se creuse</b>&nbsp;: la "
        "part encaissée est passée de 80&nbsp;% en 2021 à 67&nbsp;% en 2025, "
        "pendant que le montant annoncé, lui, monte.",
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
                ("2024", "16,7 Md&nbsp;€", "11,4 Md&nbsp;€", "≈ 68&nbsp;%"),
                ("<b>2025</b>", "<b>17,1 Md&nbsp;€</b>", "<b>11,4 Md&nbsp;€</b>",
                 "<b>≈ 67&nbsp;%</b>"),
            ),
            ("date", "nombre", "nombre", "nombre"),
        )
        + "<p>Le montant annoncé est un mauvais indicateur pour une seconde "
        "raison, que la Cour des comptes établit en décembre&nbsp;2025&nbsp;: "
        "<b>rapporté aux recettes fiscales, le rendement du contrôle recule</b>"
        " — de 4,3&nbsp;% en 2015 à 2,8&nbsp;% en 2024. Il progresse en euros "
        "courants et décroît en proportion de ce qu'il devrait protéger.</p>",
        "Chiffres des rapports d'activité et communiqués annuels de la "
        "DGFiP&nbsp;; les périmètres de publication ont évolué sur la période, "
        "et les montants encaissés une année donnée portent en partie sur des "
        "contrôles antérieurs. À lire comme une tendance, pas comme une "
        "comptabilité. Voir <a href=\"sources.html#fiscal\">Sources</a>.",
        "controle",
    )

    corps += cle(
        "Et la fraude sociale ?",
        "Elle est réelle, elle est mieux mesurée que la fraude fiscale, et "
        "elle reste <b>plus petite d'un ordre de grandeur</b> que ce qui "
        "échappe aux prélèvements. Le dire n'est pas l'excuser&nbsp;: c'est "
        "refuser de se tromper de cible.",
        tableau(
            "Fraude sociale : estimations et montants détectés",
            ("Poste", "Source", "Nature", "Montant"),
            (
                ("<b>Fraude sociale, toutes natures</b>", "HCFiPS, 2025",
                 "Estimation&nbsp;; 17,5&nbsp;Md&nbsp;€ si l'on y ajoute les "
                 "erreurs de bonne foi", "<b>≈ 14 Md&nbsp;€/an</b>"),
                ("dont cotisations éludées", "HCFiPS, décembre&nbsp;2024",
                 "Travail dissimulé, salariés du privé non agricole",
                 "6 à 7,8 Md&nbsp;€/an"),
                ("dont prestations familiales et RSA", "CNAF",
                 "Préjudice estimé par la caisse", "≈ 2,5 à 3 Md&nbsp;€/an"),
                ("Travail dissimulé redressé", "URSSAF, 2025",
                 "Redressements notifiés", "1,5 Md&nbsp;€"),
                ("Toutes branches", "Sécurité sociale, 2024",
                 "Fraude <b>détectée et redressée</b>", "≈ 2,9 Md&nbsp;€"),
                ("<b>Pour mémoire&nbsp;:</b> non-recours au RSA",
                 "DREES, mai&nbsp;2026",
                 "Foyers éligibles ne percevant pas la prestation (fin 2021)",
                 "33 à 37&nbsp;%, soit ≈ 560&nbsp;000 foyers"),
            ),
            ("texte", "texte", "long", "nombre"),
        ),
        "Deux remarques. La fraude sociale est <b>mieux estimée que la fraude "
        "fiscale</b> — il existe un chiffre annuel, révisé, discuté&nbsp;; "
        "c'est exactement ce qui manque de l'autre côté, et cela montre que "
        "notre mesure n°&nbsp;8 n'a rien d'irréaliste. Et la dernière ligne "
        "n'est pas une provocation&nbsp;: un tiers d'allocataires qui ne "
        "réclament pas ce à quoi ils ont droit est le symptôme de la même "
        "complexité. Voir <a href=\"sources.html#social\">Sources</a>.",
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
                ("<b>2025</b>", "<b>66</b>", "<b>27ᵉ sur 182</b>"),
            ),
            ("date", "nombre", "nombre"),
        )
        + "<p>L'indice mesure une <b>perception</b> par des experts et des "
        "milieux d'affaires, pas un nombre d'actes&nbsp;: il ne dit pas "
        "combien on vole, il dit ce que l'on croit. C'est une limite, et elle "
        "vaut d'être écrite. Une seconde&nbsp;: Transparency International "
        "recommande de comparer <b>les notes et non les rangs</b>, le nombre "
        "de pays évalués et les sources retenues variant d'un millésime à "
        "l'autre. Ce qui est significatif ici, c'est donc le passage de 72 à "
        "66 en trois ans — pas le recul de six places, que nous donnons pour "
        "mémoire. Deux autres signaux complètent le tableau&nbsp;:</p>"
        "<p>— le <b>GRECO</b>, organe anticorruption du Conseil de l'Europe, "
        "classe la France en conformité seulement <i>partielle</i> sur la "
        "majorité des recommandations de son cinquième cycle, qui porte sur "
        "les hautes fonctions de l'exécutif et les services répressifs&nbsp;;<br>"
        "— la justice condamne, d'après l'analyse de l'AFA portant sur "
        "2016-2022, de l'ordre de <b>400 infractions par an</b> au titre des "
        "atteintes à la probité — corruption, favoritisme, prise illégale "
        "d'intérêts, détournement de fonds publics —, soit environ "
        "3&nbsp;000 sur la période et 502 pour la seule année 2022. Un ordre "
        "de grandeur sans commune mesure avec l'ampleur supposée du "
        "phénomène&nbsp;; et il s'agit d'<i>infractions</i> sanctionnées, non "
        "de personnes, une même décision pouvant en retenir plusieurs.</p>",
        "Dernier millésime repris ici&nbsp;: 2025 pour l'indice, 2022 pour "
        "les condamnations. Voir "
        "<a href=\"sources.html#corruption\">Sources</a>.",
        "corruption",
    )

    corps += cle(
        "Où la corruption se joue-t-elle ?",
        "Dans la <b>commande publique</b>, d'abord&nbsp;: "
        "233&nbsp;milliards d'euros recensés en 2024, près de 8&nbsp;% du PIB, "
        "et le premier poste de risque identifié par toutes les évaluations.",
        "<p>La Commission européenne estimait en 2014 le coût de la corruption "
        "pour l'Union à environ <b>120&nbsp;milliards d'euros par an</b>&nbsp;; "
        "une étude du Parlement européen de 2016, retenant un périmètre plus "
        "large, aboutissait à une fourchette de <b>179 à 990&nbsp;milliards</b>. "
        "L'écart de un à huit entre deux travaux européens — l'un de la "
        "Commission, l'autre du Parlement — dit l'état réel de la "
        "connaissance.</p>"
        "<p><b>Une démonstration, offerte par le recensement lui-même.</b> Le "
        "montant recensé bondit de ≈ 160 à 233&nbsp;Md&nbsp;€ en 2024 — non "
        "parce que l'achat public aurait explosé, mais parce que le seuil de "
        "déclaration obligatoire est passé de 90&nbsp;000 à "
        "40&nbsp;000&nbsp;€. Soixante-dix milliards d'euros de contrats "
        "existaient déjà&nbsp;; ils n'étaient simplement pas comptés. C'est "
        "tout l'argument de ce site en une ligne&nbsp;: <i>on ne connaît que "
        "ce que l'on mesure</i>. Le secteur public <b>local</b> en concentre "
        "100,7&nbsp;Md&nbsp;€, soit 43&nbsp;% du total.</p>"
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
             "Aucune estimation officielle, aucune série — la Cour des comptes "
             "le constate encore en décembre&nbsp;2025, hors travaux "
             "préliminaires sur la seule TVA. Une <b>trentaine "
             "d'administrations de l'OCDE</b> en publient un régulièrement, "
             "dont le Royaume-Uni depuis 2005."),
            ("Combien de fraude est détectée, rapportée à la fraude commise&nbsp;?",
             "Inconnu, faute de dénominateur. On publie le numérateur — les "
             "montants détectés — et on l'appelle un résultat."),
            ("Quel est le taux de recouvrement effectif, service par service&nbsp;?",
             "Agrégé au niveau national, jamais détaillé publiquement."),
            ("Combien coûtent les 465 dépenses fiscales, et lesquelles sont "
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

    corps += """
<p><b>Une objection nous est faite ici, et elle est juste&nbsp;:</b> le plan
antifraude de 2023 a créé un <i>conseil d'évaluation des fraudes</i>, chargé
précisément de produire ces estimations. Nous en prenons acte. Mais un conseil
qui délibère n'est pas une série publiée&nbsp;: <b>deux ans après son
installation, la Cour des comptes constate en décembre&nbsp;2025 qu'il n'existe
toujours pas d'estimation de l'écart fiscal</b>, hors travaux préliminaires sur
la seule TVA déclarée. Tant qu'il n'y a pas d'estimation annuelle, de méthode
publiée et critiquable, révisable d'un exercice à l'autre et débattue au
Parlement avant le vote du budget, le dénominateur manque. C'est la différence
entre une instance et une statistique, et c'est tout l'objet de la mesure
n°&nbsp;8.</p>
"""

    corps += vigilance(
        "<b>Une estimation n'est pas une mesure.</b> Toute la difficulté de "
        "cette page tient en une phrase&nbsp;: on ne connaît que la fraude que "
        "l'on a détectée, et détecter davantage fait monter les chiffres sans "
        "que la fraude ait bougé. C'est pourquoi nous ne prétendons pas "
        "« récupérer 100&nbsp;milliards » — et pourquoi notre premier "
        "engagement porte sur la mesure elle-même. Les critiques adressées à "
        "cette page sont traitées sur "
        "<a href=\"objections.html#chiffrage\">Objections</a>."
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
         "Cumul des 22 CJIP conclues entre 2016 et décembre&nbsp;2024, dont "
         "2,08&nbsp;Md&nbsp;€ pour la seule affaire Airbus (2020)."),
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
             "≈ 10&nbsp;000 agents dédiés au contrôle&nbsp;: −19&nbsp;% "
             "entre 2015 et 2024 (Cour des comptes), sur une DGFiP qui a perdu "
             "plus de 30&nbsp;000 emplois depuis 2008"),
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
         "17,1&nbsp;Md&nbsp;€ notifiés en 2025, en hausse continue depuis "
         "2020. <b>Mais</b> la part encaissée tombe de 80&nbsp;% (2021) à "
         "67&nbsp;% (2025), et le rendement rapporté aux recettes fiscales "
         "recule de 4,3&nbsp;% (2015) à 2,8&nbsp;% (2024)."),
        ("Les grandes entreprises transigent",
         "Vingt-deux CJIP entre 2016 et 2024, ≈ 4&nbsp;Md&nbsp;€ d'amendes. "
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
        "règles illisibles, multiplie les régimes voisins aux prélèvements "
        "très différents, garde ses données pour lui et contrôle ses propres "
        "poursuites fabrique de la fraude plus vite qu'il n'en réprime.",
    )

    corps += plan((
        ("complexite", "La complexité"),
        ("tiers", "La déclaration par un tiers"),
        ("recouvrement", "Le recouvrement"),
        ("opacite", "L'opacité"),
        ("poursuites", "Les poursuites"),
        ("moyens", "Les moyens"),
        ("alerte", "L'alerte"),
    ))

    corps += reperes((
        ("Dépenses fiscales recensées", "465",
         "Pour 88,3&nbsp;Md&nbsp;€ en 2026&nbsp;: autant de régimes "
         "particuliers, autant de frontières à contourner (annexe « Voies et "
         "moyens » du projet de loi de finances pour 2026)."),
        ("Taux de prélèvements obligatoires", "43,6 % du PIB",
         "En 2025, net des crédits d'impôt (Insee). Selon la définition "
         "d'Eurostat, qui inclut les cotisations imputées&nbsp;: 45,3&nbsp;% "
         "en 2024, <b>deuxième rang de l'Union derrière le Danemark</b> "
         "(45,8&nbsp;%)."),
        ("Part des redressements jamais encaissée", "≈ 33 %",
         "En 2025. Elle n'était que de 20&nbsp;% en 2021&nbsp;: l'écart se "
         "creuse (DGFiP)."),
        ("Registre des bénéficiaires effectifs", "fermé",
         "Accès public restreint depuis l'arrêt de la CJUE de "
         "novembre&nbsp;2022&nbsp;; le délai européen de réouverture aux "
         "porteurs d'un intérêt légitime a expiré le 10&nbsp;juillet&nbsp;2026."),
    ))

    corps += cle(
        "1. Une règle illisible est une règle qu'on contourne",
        "La fraude n'est pas seulement un choix moral&nbsp;: c'est souvent un "
        "<b>arbitrage de frontière</b>. Plus il y a de régimes particuliers, "
        "plus il y a de frontières, et plus il est facile de se ranger du bon "
        "côté d'une ligne qu'on a soi-même dessinée.",
        "<p>465 dépenses fiscales pour 88,3&nbsp;milliards d'euros en 2026, "
        "un code général des impôts de plusieurs milliers de pages, un "
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
        "2. Ce qui protège l'impôt, c'est la déclaration par un tiers",
        "La régularité la mieux établie de toute la littérature n'est pas "
        "celle du taux&nbsp;: <b>là où un employeur ou une banque déclare à la "
        "place du contribuable, la fraude est marginale&nbsp;; là où l'on "
        "s'auto-déclare, elle est massive</b> — à barème identique.",
        "<p>Le contraste a été mesuré, et il est spectaculaire&nbsp;: sur les "
        "revenus déclarés par un tiers, l'écart entre l'impôt dû et l'impôt "
        "payé se compte en fractions de point&nbsp;; sur les revenus "
        "auto-déclarés, il se compte en dizaines de points. Même contribuable, "
        "même barème, même administration — seule change la personne qui "
        "remplit la case.</p>"
        "<p>Ce résultat commande le programme entier. La mesure n°&nbsp;3 — "
        "verser les prestations à partir de données qu'un employeur a déjà "
        "déclarées — n'est pas une mesure de confort&nbsp;: c'est "
        "l'application directe de la seule chose que l'on sache faire contre "
        "la fraude déclarative. Et la mesure n°&nbsp;1 s'y rattache&nbsp;: "
        "chaque régime particulier ouvre une zone où plus aucun tiers ne "
        "déclare, et où il faut donc croire sur parole.</p>"
        "<p><b>Et le niveau des prélèvements&nbsp;?</b> Nous avons d'abord "
        "écrit ici que la France prélevant au plus haut niveau de l'Union — "
        "elle est en réalité <b>deuxième</b>, à 45,3&nbsp;% du PIB en 2024 "
        "selon Eurostat, derrière le Danemark et ses 45,8&nbsp;% —, un "
        "taux élevé appelait mécaniquement la fraude. C'est plus incertain "
        "que nous ne l'avions écrit, et il faut le dire&nbsp;: dans le modèle "
        "d'Allingham et Sandmo (1972) que nous invoquions, le signe de cet "
        "effet est ambigu, et Yitzhaki (1974) montre que lorsque la pénalité "
        "est proportionnelle à l'impôt éludé — le cas français —, une hausse "
        "du taux peut au contraire <i>réduire</i> la fraude.</p>"
        "<p>Ce qui reste solide, c'est l'effet des <b>écarts</b> de taux, et "
        "non celui de leur niveau. Quand un même travail supporte des "
        "prélèvements qui varient de plusieurs dizaines de points selon qu'il "
        "est salarié, auto-entrepreneur, en portage ou sur plateforme, "
        "l'arbitrage n'est plus moral&nbsp;: il est offert par la règle. C'est "
        "cette dispersion-là, et non la moyenne, qui fabrique du travail "
        "dissimulé.</p>"
        "<p class=\"discret\">Corollaire, et il oriente tout le bloc I du "
        "programme&nbsp;: on ne réduit pas la fraude en baissant un taux "
        "moyen, mais en supprimant les écarts entre régimes voisins et en "
        "étendant la déclaration par un tiers partout où elle est "
        "techniquement possible.</p>",
        "Sur la correction apportée à cette section et sur l'objection qui "
        "l'a provoquée, voir <a href=\"objections.html#taux\">Objections</a>.",
        "tiers",
    )

    corps += cle(
        "3. On notifie, on n'encaisse pas",
        "L'administration annonce un montant de redressements qui monte "
        "— 17,1&nbsp;Md&nbsp;€ en 2025. La part qu'elle encaisse, elle, "
        "descend&nbsp;: <b>de 80&nbsp;% en 2021 à 67&nbsp;% en 2025</b>. "
        "Entreprises liquidées, avoirs déplacés, contentieux qui s'éternisent. "
        "Le chiffre annoncé n'est pas le chiffre rentré, et l'écart grandit.",
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
        "permis la plupart des révélations de la décennie. Le paquet "
        "anti-blanchiment de 2024 organise sa réouverture aux porteurs d'un "
        "intérêt légitime&nbsp;: le délai de transposition de ces articles a "
        "expiré le <b>10&nbsp;juillet&nbsp;2026</b>, et le registre n'est "
        "toujours pas rouvert.</p>"
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
        "Les effectifs du contrôle fiscal ont baissé de <b>19&nbsp;% entre "
        "2015 et 2024</b> — le chiffre est de la Cour des comptes, "
        "décembre&nbsp;2025. Le plan de 2023 promet 1&nbsp;500 agents d'ici "
        "2027&nbsp;: cela ne rattrape pas ce qui a été perdu.",
        "<p>Le contraste est plus net encore sur le versant anticorruption. "
        "L'Agence française anticorruption compte de l'ordre de 50 agents pour "
        "contrôler les programmes de conformité de milliers d'entreprises et "
        "de collectivités. La Haute Autorité pour la transparence de la vie "
        "publique en compte une soixantaine pour ≈ 16&nbsp;000 déclarants. Le "
        "parquet national financier, une vingtaine de magistrats pour des "
        "centaines de procédures, souvent internationales.</p>"
        "<p>Le même reflux se lit du côté pénal, et la Cour des comptes le "
        "documente&nbsp;: les poursuites pour fraude fiscale sont passées de "
        "plus de <b>850 par an avant 2018 à environ 700 en 2023-2024</b>, et "
        "le taux moyen des sanctions fiscales est tombé de 30&nbsp;% de "
        "l'impôt éludé en 2015 à <b>15&nbsp;% dix ans plus tard</b>. Pendant "
        "que le discours durcit, la sanction s'allège.</p>"
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
# 5. Programme — les douze mesures
# ---------------------------------------------------------------------------

def programme() -> str:
    corps = affiche(
        "La proposition libérale",
        "Douze mesures.<br>Aucune n'ajoute<br>"
        '<span class="cle-texte">une agence.</span>',
        "Trois blocs, dans l'ordre où ils doivent être menés&nbsp;: assécher "
        "la fraude en simplifiant la règle, l'exposer en publiant tout ce qui "
        "est public — à commencer par l'argent de la vie politique —, la "
        "sanctionner en rendant les poursuites indépendantes et le "
        "recouvrement mesurable. Chaque mesure dit ce qu'elle remplace.",
    )

    corps += plan((
        ("assecher", "Assécher"),
        ("exposer", "Exposer"),
        ("sanctionner", "Sanctionner"),
        ("calendrier", "Le calendrier"),
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
         "<p><b>Le mécanisme, et non la liste.</b> Toute dépense fiscale est "
         "créée pour quatre ans au plus et s'éteint d'elle-même à ce terme, "
         "sauf re-vote appuyé sur une évaluation indépendante publiée six "
         "mois avant l'échéance. La charge de la preuve change de camp&nbsp;: "
         "ce n'est plus à qui veut supprimer une niche de démontrer qu'elle "
         "est inutile, c'est à qui veut la garder de démontrer qu'elle sert. "
         "La liste des suppressions n'est donc pas arrêtée dans ce "
         "programme&nbsp;: elle sort de l'évaluation, et elle est "
         "publique.</p>"
         "<p>Une assiette large et des régimes voisins peu dissemblables "
         "produisent mécaniquement moins de frontières à contourner, moins de "
         "contentieux, et moins de fraude involontaire.</p>",
         "465 dépenses fiscales pour 88,3&nbsp;Md&nbsp;€ en 2026, recensées "
         "chaque année dans l'annexe « Voies et moyens » du budget, et dont "
         "une minorité seulement a fait l'objet d'une évaluation."),

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
         "partie du non-recours. Trois problèmes, une seule cause.</p>"
         "<p><b>La limite, et il faut l'écrire.</b> La déclaration sociale "
         "nominative ne connaît que ce qu'un employeur déclare. Les revenus "
         "des indépendants, ceux du capital, les pensions alimentaires et le "
         "patrimoine restent déclaratifs. La mesure couvre donc d'emblée la "
         "majorité des situations, pas leur totalité — et la part "
         "déclarative résiduelle doit être réduite dans le même mouvement, "
         "source par source, à mesure qu'un tiers peut déclarer à la place de "
         "l'allocataire.</p>",
         "l'allocataire déclare lui-même ses ressources, plusieurs fois par "
         "an&nbsp;; la DREES estime en mai&nbsp;2026 que 33 à 37&nbsp;% des "
         "foyers éligibles au RSA ne le perçoivent pas — environ "
         "560&nbsp;000 foyers —, pendant que les caisses poursuivent des "
         "indus qu'elles ont elles-mêmes provoqués."),
    ))

    corps += """
<h2 id="exposer" tabindex="-1">Bloc II — Exposer <span class="badge proposition">Proposition</span></h2>
<p>Ce qui est financé par l'impôt appartient à ceux qui le paient. La
publication n'est pas une faveur faite aux curieux&nbsp;: c'est le seul contrôle
qui passe à l'échelle, parce qu'il mobilise des milliers de regards au lieu de
cinquante agents.</p>
<p>Deux de ces cinq mesures portent sur les responsables publics eux-mêmes —
l'argent des campagnes et le passage vers le privé. Elles ne figuraient pas
dans la première version de ce programme, et leur absence était sa faiblesse la
plus visible&nbsp;: un parti qui réclame la traçabilité de l'argent public et
ne commence pas par le sien ne mérite pas d'être cru.</p>
"""
    corps += mesures((
        ("Publier 100 % de la dépense publique en données ouvertes",
         "<p>Marchés, subventions, aides aux entreprises, dépenses de l'État "
         "et des collectivités&nbsp;: chaque engagement est publié dans les "
         "trente jours, en format ouvert et lisible par une machine, sur un "
         "portail unique. Les marchés suivent le standard international "
         "<i>Open Contracting Data Standard</i>, avenants et sous-traitants "
         "compris. Le non-respect prive l'acte de force exécutoire.</p>"
         "<p>L'obligation vaut pour l'État <b>comme pour les "
         "collectivités</b>&nbsp;: l'essentiel des marchés et la majorité des "
         "condamnations pour atteinte à la probité relèvent de l'échelon "
         "local, et un portail qui s'arrêterait à l'État manquerait son "
         "objet.</p>"
         "<p>Le précédent ukrainien — <i>Prozorro</i>, et son outil de "
         "signalement citoyen <i>DoZorro</i> — montre qu'une plateforme "
         "ouverte change le comportement des acheteurs avant même qu'un "
         "contrôle ait lieu. On nous objectera le classement de l'Ukraine, et "
         "c'est justement l'argument&nbsp;: un dispositif qui produit un effet "
         "mesurable dans un environnement hostile en produira un ici. Citer "
         "le Danemark ne prouverait rien.</p>",
         "les données existent mais sont dispersées entre des centaines de "
         "profils d'acheteurs, publiées avec retard, dans des formats "
         "hétérogènes, et souvent sans les avenants."),

        ("Rendre visible qui détient quoi, et où",
         "<p><b>Le registre des bénéficiaires effectifs</b>&nbsp;: accès de "
         "plein droit, gratuit et traçable, pour les journalistes, les "
         "chercheurs, les ONG et les entreprises soumises à des obligations "
         "de vigilance — exactement le cadre que la Cour de justice de "
         "l'Union européenne a jugé proportionné, et que le paquet "
         "anti-blanchiment européen de 2024 organise. Le délai de "
         "transposition de ces articles a <b>expiré le "
         "10&nbsp;juillet&nbsp;2026</b> et le registre n'est toujours pas "
         "rouvert&nbsp;: il ne s'agit donc plus de choisir, mais de rattraper "
         "un retard — au maximum de ce que le droit permet, et non au "
         "minimum.</p>"
         "<p><b>La déclaration pays par pays</b>&nbsp;: le droit européen "
         "impose déjà aux grands groupes de publier où ils réalisent leur "
         "chiffre d'affaires et où ils paient leur impôt. La France retient "
         "le périmètre le plus large que la directive autorise et publie ces "
         "déclarations en données ouvertes, sur le portail unique, plutôt "
         "qu'en documents dispersés que personne ne peut agréger.</p>"
         "<p>Aucune de ces deux obligations n'est nouvelle&nbsp;: l'une et "
         "l'autre rendent consultable ce qui est déjà déclaré.</p>",
         "l'accès du grand public au registre est restreint depuis l'arrêt de "
         "la CJUE de novembre&nbsp;2022, l'outil qui avait permis l'essentiel "
         "des révélations de la décennie est devenu difficile d'accès, et le "
         "délai européen de réouverture est dépassé depuis le "
         "10&nbsp;juillet&nbsp;2026&nbsp;; "
         "les déclarations pays par pays existent mais sont publiées en ordre "
         "dispersé, sans format commun ni point d'accès unique."),

        ("Publier l'argent de la vie politique, à commencer par le nôtre",
         "<p>Comptes de campagne et comptes des partis publiés en données "
         "ouvertes, au même format et dans les mêmes délais que le reste de "
         "la dépense publique. La Commission nationale des comptes de "
         "campagne reçoit les moyens de contrôler sur pièces, et publie ses "
         "contrôles — pas seulement ses décisions.</p>"
         "<p>Frais de mandat des parlementaires et des exécutifs locaux&nbsp;: "
         "publication annuelle, poste par poste, exactement ce que nous "
         "demandons aux acheteurs publics. Et un registre consultable de "
         "l'exécution des peines d'inéligibilité, qui n'existe pas "
         "aujourd'hui.</p>"
         "<p><b>Nous appliquons cette mesure à nos propres comptes sans "
         "attendre la loi.</b> Un parti qui réclame la traçabilité de "
         "l'argent public et ne publie pas le sien n'est pas crédible une "
         "minute, et l'objection nous serait faite le premier jour — elle "
         "l'a d'ailleurs été.</p>",
         "les comptes de campagne sont déposés à la CNCCFP et publiés sous "
         "forme agrégée&nbsp;; les frais de mandat sont contrôlés à "
         "l'intérieur de chaque assemblée, sans publication détaillée&nbsp;; "
         "et aucun registre public ne permet de savoir qui exécute une peine "
         "d'inéligibilité."),

        ("Fermer la porte tournante : publier tous les avis de déontologie",
         "<p>Tous les avis rendus sur le départ d'un responsable public vers "
         "le privé sont publiés intégralement, réserves comprises, et non "
         "sous forme de statistiques annuelles. Le délai de carence est porté "
         "à cinq ans pour les fonctions de régulation, d'achat public et de "
         "contrôle — celles où l'information emportée a une valeur "
         "marchande.</p>"
         "<p>Surtout, le manquement cesse de relever de la seule voie pénale, "
         "qui n'est presque jamais empruntée&nbsp;: l'autorité prononce "
         "elle-même une sanction financière, publique et proportionnée à la "
         "rémunération obtenue.</p>"
         "<p>La Haute Autorité existe et fait son travail. Nous lui donnons "
         "la publicité et la sanction qui lui manquent&nbsp;: ce n'est pas "
         "une agence de plus, c'est la même avec des dents.</p>",
         "le pantouflage figure depuis dix ans parmi les trois reproches "
         "constants du GRECO à la France&nbsp;; les avis ne sont pas tous "
         "publiés, la carence est de trois ans, et le manquement relève d'une "
         "infraction pénale rarement poursuivie."),

        ("Publier chaque année un chiffrage officiel de la fraude",
         "<p>Un <i>écart fiscal et social</i> à la française&nbsp;: une "
         "estimation annuelle de la différence entre ce qui est dû et ce qui "
         "est perçu, produite par l'Insee avec le Conseil des prélèvements "
         "obligatoires, selon une méthode publiée et critiquable, révisable "
         "d'une année sur l'autre, et débattue au Parlement avant le vote du "
         "budget.</p>"
         "<p>C'est la mesure qui rend toutes les autres évaluables. Sans "
         "dénominateur, « un milliard récupéré » ne veut rien dire.</p>",
         "aucune estimation officielle consolidée n'existe — la Cour des "
         "comptes le constate encore en décembre&nbsp;2025 et en fait sa "
         "première recommandation&nbsp;; une trentaine d'administrations de "
         "l'OCDE en publient une, dont le Royaume-Uni depuis 2005."),
    ), depart=4)

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
         "<p><b>Et si le Congrès ne vient pas.</b> Il serait malhonnête de "
         "promettre que la révision aboutira&nbsp;: elle a été votée en termes "
         "identiques par les deux assemblées, et abandonnée avant le Congrès. "
         "Une partie de la mesure ne dépend donc pas de lui, et passe par la "
         "loi ordinaire dès la première année&nbsp;: publication de toutes "
         "les nominations du parquet, de l'avis du CSM, et — lorsque le garde "
         "des Sceaux s'en écarte — des motifs pour lesquels il s'en écarte. "
         "On ne retire pas le pouvoir de nommer&nbsp;; on oblige son exercice "
         "à se justifier, ce qui n'est pas rien.</p>"
         "<p>S'y ajoute un objectif de délai&nbsp;: une procédure financière "
         "qui dure plus de cinq ans fait l'objet d'un rapport public du "
         "ministère public expliquant pourquoi.</p>",
         "le garde des Sceaux nomme les procureurs&nbsp;; il suit l'avis du "
         "CSM par convention, sans y être tenu en droit."),

        ("Une prime au lanceur d'alerte, jusqu'à 30 % des sommes recouvrées",
         "<p>Barème public et progressif, versé uniquement sur les sommes "
         "<b>effectivement encaissées</b>, plafonné, ouvert à la fraude "
         "fiscale et sociale <b>organisée</b> et aux atteintes à la probité "
         "dans la commande publique. La décision appartient à une autorité "
         "indépendante existante, pas à l'administration bénéficiaire.</p>"
         "<p><b>Ce que la prime n'est pas.</b> Elle ne vise ni l'allocataire "
         "ni le voisin&nbsp;: les dossiers individuels de prestations en sont "
         "exclus par construction, et un seuil de préjudice élevé, fixé par "
         "la loi, en ferme l'accès. La différence entre l'alerte et la "
         "délation n'est pas morale, elle est mécanique — elle tient au "
         "seuil, au champ et à qui décide. Un salarié qui documente une "
         "entente sur un marché de 200&nbsp;M&nbsp;€ apporte ce qu'aucun "
         "contrôle de routine ne trouvera&nbsp;; une dénonciation de "
         "voisinage n'apporte rien qu'une caisse ne sache vérifier "
         "seule.</p>"
         "<p>En regard, une protection réelle&nbsp;: prise en charge des frais "
         "de procédure dès la recevabilité du signalement, et sanction "
         "financière dissuasive des représailles et des procédures-bâillons.</p>",
         "l'aviseur fiscal rémunéré existe depuis 2017, mais son indemnisation "
         "est discrétionnaire, sans barème public, et d'un champ étroit."),

        ("Rendre l'exclusion des marchés effective, et vérifiable",
         "<p>L'exclusion après condamnation définitive existe déjà en "
         "droit&nbsp;; ce qui manque, c'est de savoir qui est exclu. Un "
         "<b>registre public</b>, tenu par l'AFA, dit à tout acheteur la "
         "situation d'un candidat. Sans lui, l'exclusion est une règle que "
         "personne n'est en mesure d'appliquer.</p>"
         "<p>Le vrai trou, c'est la convention judiciaire d'intérêt public. "
         "Une exclusion automatique après CJIP se heurterait à la "
         "présomption d'innocence, la convention étant sans reconnaissance de "
         "culpabilité&nbsp;: nous proposons donc l'inverse&nbsp;: faire de "
         "l'exclusion, et de sa durée, <b>un terme négocié de la convention "
         "elle-même</b>, homologué par le juge qui la valide. L'entreprise "
         "sait ce qu'elle signe, et le juge en répond.</p>"
         "<p>L'exclusion se lève par décision motivée et publiée si "
         "l'entreprise démontre avoir remédié aux défaillances — le mécanisme "
         "existe déjà en droit européen. La CJIP reste&nbsp;: c'est un bon "
         "outil. Mais une amende que l'entreprise provisionne ne change pas "
         "un modèle d'affaires&nbsp;; la perte de l'accès aux marchés, si.</p>",
         "l'exclusion existe pour les condamnations définitives (art. "
         "L.&nbsp;2141-1 du code de la commande publique), mais aucun registre "
         "ne permet à l'acheteur de la vérifier&nbsp;; et la CJIP, qui éteint "
         "les poursuites sans reconnaissance de culpabilité, n'en emporte "
         "aucune — l'entreprise peut soumissionner le lendemain."),

        ("Mesurer le recouvrement, pas les annonces",
         "<p>Publication trimestrielle, service par service, du montant "
         "notifié, du montant encaissé et du délai moyen&nbsp;; les objectifs "
         "des administrations et l'intéressement de leurs directions portent "
         "sur l'encaissement. Généralisation des saisies conservatoires dès "
         "l'engagement du contrôle, et extension du périmètre de l'AGRASC à la "
         "fraude fiscale et sociale organisée.</p>",
         "l'indicateur public est le montant notifié&nbsp;; le tiers jamais "
         "encaissé n'apparaît dans aucune série détaillée."),
    ), depart=9)

    corps += '<h2 id="calendrier" tabindex="-1">Le calendrier, et comment nous juger</h2>'
    corps += """
<p>Un programme sans échéance ni indicateur n'est pas réfutable, et ce qui
n'est pas réfutable n'a pas à être cru. Voici ce qui doit être vrai, à quelle
date, et où le vérifier — sur des sources qui ne sont pas les nôtres.</p>
"""
    corps += tableau(
        "Ce qui doit être vrai, et quand",
        ("Échéance", "Ce qui doit être vrai", "Où le vérifier"),
        (
            ("6 mois",
             "Le rescrit de droit sous trois mois est voté&nbsp;; les marchés "
             "de l'État sont publiés au standard <i>Open Contracting</i> sur "
             "un portail unique&nbsp;; nos propres comptes sont en ligne.",
             "Légifrance, le portail, notre dépôt"),
            ("1 an",
             "Une première estimation de l'écart fiscal et social est "
             "publiée, même provisoire, avec sa méthode&nbsp;; le registre des "
             "bénéficiaires effectifs est rouvert&nbsp;; tous les avis de "
             "déontologie sont publiés.",
             "Insee, INPI, HATVP"),
            ("3 ans",
             "Les prestations sous condition de ressources sont versées à "
             "la source pour les revenus salariés&nbsp;; la part encaissée des "
             "redressements est publiée chaque trimestre, service par "
             "service&nbsp;; le registre des exclusions de la commande "
             "publique est ouvert.",
             "CNAF et CNAM, DGFiP, AFA"),
            ("5 ans",
             "Le nombre de dépenses fiscales est divisé par deux à rendement "
             "restitué&nbsp;; la part encaissée dépasse 80&nbsp;% sur trois "
             "exercices consécutifs&nbsp;; l'écart fiscal publié est orienté à "
             "la baisse sur la série.",
             "Annexe « Voies et moyens », DGFiP, Insee"),
        ),
        ("date", "long", "texte"),
    )
    corps += """
<p class="discret">Si ces repères ne sont pas atteints, ils seront publics et
la comparaison sera possible&nbsp;: c'est le but. Un programme qui ne se donne
pas les moyens d'avoir tort demande une confiance qu'il n'a pas méritée.</p>
"""

    corps += cle(
        "Ce que nous refusons",
        "Un programme libéral contre la fraude ne peut pas être un programme "
        "de surveillance. Cinq lignes que nous ne franchirons pas — et il "
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
        "intérêts des décideurs, bénéficiaires effectifs des sociétés, et "
        "l'argent de nos propres campagnes. Pas des données personnelles des "
        "citoyens ordinaires.</p>"
        "<p><b>La prime à la délation ordinaire.</b> La récompense du "
        "signalement s'arrête où commence le voisinage&nbsp;: seuil élevé, "
        "champ limité aux montages organisés et à la commande publique, "
        "dossiers individuels de prestations exclus. Une politique qui "
        "paierait la dénonciation du quotidien n'aurait pas le même objet, et "
        "nous n'en voulons pas.</p>",
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
  compris quand il est faible. La page <a href="objections.html">Objections</a>
  traite ensuite les neuf critiques les plus solides qui nous sont faites, dont
  quatre qui portent.</p>
  <p class="actions"><a class="bouton" href="chiffrage.html">Voir le chiffrage</a>
  <a class="bouton second" href="objections.html">Lire les objections</a></p>
</div>
"""

    return page(
        "programme.html",
        "Programme — douze mesures libérales contre la fraude et la corruption",
        "Douze mesures : simplification fiscale, prestations à la source, "
        "publication intégrale de la dépense publique, réouverture du registre "
        "des bénéficiaires effectifs, transparence de l'argent de la vie "
        "politique, encadrement du pantouflage, chiffrage annuel de la fraude, "
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
        "<strong>Le degré de confiance est affiché.</strong> Quand la "
        "fourchette est fragile, la colonne le dit et la fourchette "
        "s'élargit&nbsp;; quand nous ne savons pas chiffrer du tout, la ligne "
        "ne porte aucun montant et ne s'additionne à rien. Sur les six mesures "
        "que le tableau de rendement examine, <b>trois seulement portent un "
        "montant</b>.",
        "<strong>Nos hypothèses sont isolées et nommées.</strong> Six valeurs "
        "de cette page ne viennent pas d'une source publique&nbsp;: ce sont "
        "les nôtres. Elles sont listées à part, sur "
        "<a href=\"sources.html#hypotheses\">Sources</a>, pour être "
        "contestées une par une plutôt que fondues dans un total.",
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
<p class="discret">À comparer aux 11,4&nbsp;Md&nbsp;€ que le seul contrôle
fiscal a <b>effectivement encaissés</b> en 2025 — et non aux
17,1&nbsp;Md&nbsp;€ notifiés, car la distinction que nous demandons à l'État
vaut d'abord pour nous&nbsp;: le coût du programme représente de l'ordre de 2 à
3&nbsp;% de ce montant.</p>
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
             "effet dissuasif avant contrôle. Une baisse de 1&nbsp;% sur les "
             "233&nbsp;Md&nbsp;€ recensés en 2024 vaut 2,3&nbsp;Md&nbsp;€",
             "0,7 à 4,4 Md&nbsp;€", "Moyenne"),
            ("Recouvrement effectif renforcé",
             "Ramener <b>durablement</b> la part encaissée de 67&nbsp;% "
             "(2025) à ≈ 80&nbsp;% des montants notifiés — un niveau déjà "
             "atteint en 2019 et en 2021, ce qui rend le gain plausible mais "
             "interdit de le présenter comme acquis. La borne basse retient "
             "un simple retour au niveau de 2022",
             "1 à 2,2 Md&nbsp;€", "Moyenne"),
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
             "<b>≈ 1,9 à 7,6 Md&nbsp;€/an</b>", "Moyenne"),
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
        "<p>C'est pourquoi la mesure n°&nbsp;8 du programme — le chiffrage "
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
        "des hypothèses est sur "
        "<a href=\"sources.html#hypotheses\">Sources</a>, les critiques qui "
        "nous sont faites sur <a href=\"objections.html#maigre\">Objections</a>, "
        "et une erreur se signale sur le dépôt, où elle se corrige."
    )

    return page(
        "chiffrage.html",
        "Chiffrage — ce que coûte et ce que peut rapporter le programme",
        "Le coût annuel et le rendement possible de chacune des douze mesures, "
        "avec le degré de confiance associé — et les raisons pour lesquelles "
        "nous refusons d'annoncer un chiffre unique.",
        corps,
    )


# ---------------------------------------------------------------------------
# 7. Objections — ce qu'on nous oppose, et ce que nous répondons
# ---------------------------------------------------------------------------

def objections() -> str:
    """Les neuf objections les plus solides, écrites du point de vue de qui les
    fait, et traitées une par une.

    C'est la page la plus utile du site et la plus désagréable à écrire. Un
    programme qui n'expose pas ce qu'on lui oppose demande qu'on le croie sur
    parole ; celui qui l'expose se prive de l'effet de surprise, et gagne le
    seul terrain qui compte. Deux règles ici : l'objection est formulée dans
    sa version FORTE, telle qu'un adversaire compétent la poserait, et quand
    elle porte, on le dit.
    """
    corps = affiche(
        "La contradiction",
        "Voici ce qu'on<br>nous oppose de<br>"
        '<span class="cle-texte">plus solide</span>',
        "Neuf objections, dans leur version la plus forte — pas la version "
        "commode. Quatre d'entre elles portent, au moins en partie, et nous "
        "le disons. Un programme qui ne publie pas ses points faibles demande "
        "qu'on le croie sur parole&nbsp;; ce n'est pas ce que nous demandons.",
    )

    corps += """
<div class="note resume">
  <p>Cette page est faite pour être utilisée contre nous. Si une objection
  manque, ou si une réponse vous paraît courte, <a href="sources.html">ouvrez
  un signalement</a>&nbsp;: elle sera ajoutée, et la réponse écrite au même
  endroit que les autres.</p>
</div>
"""

    corps += plan((
        ("chiffrage", "« Vous chiffrez l\'inchiffrable »"),
        ("maigre", "« Deux milliards, c\'est dérisoire »"),
        ("cadeau", "« Un cadeau fiscal déguisé »"),
        ("taux", "« Votre théorie du taux est fausse »"),
        ("surveillance", "« C\'est la société de surveillance »"),
        ("delation", "« La délation rémunérée »"),
        ("congres", "« Vous promettez l\'impossible »"),
        ("ukraine", "« Vous citez l\'Ukraine en modèle »"),
        ("nous", "« Et vos propres comptes ? »"),
    ))

    corps += cle(
        "« Vous dites que personne ne sait mesurer la fraude, et vous la chiffrez »",
        "L'objection est exacte, et c'est pourquoi nous ne chiffrons pas la "
        "fraude&nbsp;: nous chiffrons <b>l'effet de douze mesures</b>, ce qui "
        "n'est pas la même chose.",
        "<p>Un rendement n'a pas besoin d'une assiette connue pour être "
        "estimé, s'il passe par un canal observable. Nous n'écrivons jamais "
        "« la fraude coûte X, nous en récupérerons Y&nbsp;% ». Nous écrivons "
        "« la part encaissée des redressements est de 67&nbsp;%, la porter à "
        "80&nbsp;% vaut tant » — une règle de trois sur deux nombres "
        "publiés.</p>"
        "<p>Là où ce canal n'existe pas, la ligne ne porte aucun montant. Sur "
        "les six mesures que notre tableau de rendement examine, <b>trois "
        "seulement portent un chiffre</b>&nbsp;; les trois autres disent "
        "pourquoi elles n'en portent pas — effet net incertain, rendement "
        "neutre par construction, rendement nul par nature. C'est précisément "
        "ce qu'un chiffrage malhonnête ne fait jamais.</p>"
        "<p>Reste que l'objection touche un point réel&nbsp;: <b>tant que "
        "l'écart fiscal n'est pas publié, personne — nous compris — ne peut "
        "dire quelle fraction du problème ce programme traite.</b> C'est la "
        "raison d'être de la mesure n°&nbsp;8, et la raison pour laquelle elle "
        "n'est pas négociable.</p>",
        "Voir le détail ligne à ligne sur <a href=\"chiffrage.html\">Chiffrage</a>, "
        "et nos hypothèses sur <a href=\"sources.html#hypotheses\">Sources</a>.",
        "chiffrage",
    )

    corps += cle(
        "« 1,9 à 7,6 milliards, c'est dérisoire au regard des enjeux »",
        "C'est exact, et c'est volontaire. <b>Tout programme qui annonce "
        "davantage vend une assiette pour un rendement</b> — la confusion la "
        "plus répandue du débat français.",
        "<p>Les « 80 » ou « 100 milliards » qui circulent sont des estimations "
        "de ce qui échapperait à l'impôt, pas de ce qu'une politique peut "
        "faire rentrer. Une partie de ces montants est insolvable, une autre "
        "disparaît avec l'activité qui la portait, une troisième n'existerait "
        "pas sous un régime fiscal différent. Aucun pays, y compris ceux qui "
        "mesurent leur écart fiscal depuis vingt ans, n'en récupère la "
        "majeure partie.</p>"
        "<p>S'y ajoute ce que nous ne chiffrons pas, faute de canal "
        "observable&nbsp;: la fraude découragée avant d'être commise, le "
        "contentieux évité par un droit opposable, l'indu de bonne foi qui "
        "cesse d'exister. Ces effets sont probablement supérieurs aux nôtres. "
        "Nous ne les comptons pas, parce que nous ne savons pas les "
        "compter.</p>"
        "<p>Enfin, la comparaison qui compte n'est pas au montant de la "
        "fraude&nbsp;: elle est au coût. Un programme qui coûte de 215 à "
        "365&nbsp;M&nbsp;€ par an et en rapporte de 1,9 à "
        "7,6&nbsp;Md&nbsp;€ rapporte <b>cinq fois sa mise dans l'hypothèse la "
        "plus défavorable</b> — 1,9&nbsp;Md&nbsp;€ pour 365&nbsp;M&nbsp;€ — et "
        "trente-cinq fois dans la plus favorable. C'est la seule "
        "multiplication de cette page que nous faisons dans les deux sens, et "
        "c'est exprès.</p>",
        "",
        "maigre",
    )

    corps += cle(
        "« Supprimer des niches pour baisser les taux, c'est un cadeau fiscal "
        "déguisé en lutte contre la fraude »",
        "L'opération est <b>neutre pour les recettes par construction</b>, et "
        "cette neutralité est inscrite dans la loi organique qui porte la "
        "réforme&nbsp;: sans elle, la simplification serait une hausse d'impôt "
        "déguisée, ce que nous ne voulons pas davantage.",
        "<p>Le chiffrage l'écrit noir sur blanc&nbsp;: la ligne « réduction "
        "des dépenses fiscales » vaut <i>zéro</i> dans notre rendement. Nous "
        "ne finançons rien avec. Si nous voulions un cadeau fiscal, nous "
        "proposerions de baisser les taux <b>sans</b> supprimer les niches "
        "— c'est plus simple, et c'est ce que font ceux qui en veulent un.</p>"
        "<p>L'objection garde pourtant une part de vérité, et il faut la "
        "nommer&nbsp;: une opération neutre en masse ne l'est jamais pour les "
        "personnes. Supprimer une niche fait des perdants identifiables, "
        "baisser un taux fait des gagnants diffus, et rien ne garantit que ce "
        "soient les mêmes. C'est un arbitrage politique assumé, pas un effet "
        "technique&nbsp;; la publication de l'évaluation niche par niche est "
        "ce qui permet d'en débattre autrement qu'en aveugle.</p>",
        "",
        "cadeau",
    )

    corps += cle(
        "« Votre thèse selon laquelle un taux élevé nourrit la fraude est "
        "contestée par la littérature »",
        "<b>L'objection est fondée, et nous avons corrigé la page "
        "Diagnostic.</b> Dans le modèle même que nous citions, une hausse du "
        "taux peut <i>réduire</i> la fraude lorsque la pénalité est "
        "proportionnelle à l'impôt éludé — ce qui est le cas en France.",
        "<p>C'est le résultat de Yitzhaki (1974), qui corrige Allingham et "
        "Sandmo (1972). Nous avons d'abord écrit l'inverse. La cause "
        "n°&nbsp;2 du diagnostic a été réécrite autour de ce que la "
        "littérature empirique établit solidement&nbsp;: ce qui protège "
        "l'impôt, c'est <b>la déclaration par un tiers</b>. Là où un "
        "employeur ou une banque déclare à la place du contribuable, la "
        "fraude est marginale quel que soit le taux&nbsp;; là où l'on "
        "s'auto-déclare, elle est massive.</p>"
        "<p>Cette correction ne fragilise pas le programme&nbsp;: elle le "
        "renforce. Elle fonde directement la mesure n°&nbsp;3 — verser les "
        "prestations sur des données déjà déclarées par un tiers — et la "
        "mesure n°&nbsp;1, puisque ce sont les régimes particuliers qui "
        "créent les zones où plus aucun tiers ne déclare.</p>",
        "Voir la cause n°&nbsp;2 sur "
        "<a href=\"diagnostic.html#tiers\">Diagnostic</a>.",
        "taux",
    )

    corps += cle(
        "« Publier tout, croiser tous les fichiers : c'est la société de "
        "surveillance »",
        "La distinction est nette et elle tient en une ligne&nbsp;: nous "
        "demandons la publication de <b>l'argent public</b> et des "
        "<b>décideurs</b>, jamais celle des citoyens.",
        "<p>Un contrat, une subvention, une aide publique, le patrimoine d'un "
        "ministre, le bénéficiaire effectif d'une société qui soumissionne&nbsp;: "
        "tout cela est déjà, en droit, de nature publique. Un revenu "
        "d'allocataire ne l'est pas et ne le deviendra pas.</p>"
        "<p>Sur le croisement, la frontière est celle-ci&nbsp;: les données "
        "circulent <b>vers le calcul d'un droit</b>, jamais vers un score. "
        "Verser une prestation à partir de revenus déjà déclarés supprime une "
        "déclaration&nbsp;; construire un profil de risque sur des millions de "
        "personnes en ajoute une, invisible. La page Programme écrit les "
        "quatre lignes que nous ne franchirons pas, et elle les écrit "
        "<i>avant</i> qu'on nous les prête.</p>",
        "Voir « Ce que nous refusons » sur "
        "<a href=\"programme.html#refus\">Programme</a>.",
        "surveillance",
    )

    corps += cle(
        "« Payer les dénonciateurs, c'est instituer la délation »",
        "C'est pourquoi la prime <b>exclut par construction les dossiers "
        "individuels de prestations</b> et ne s'ouvre qu'au-delà d'un seuil "
        "de préjudice élevé, sur des montages organisés et sur la commande "
        "publique.",
        "<p>La différence entre l'alerte et la délation n'est pas morale, "
        "elle est mécanique&nbsp;: elle tient au seuil, au champ et à qui "
        "décide. Un salarié qui documente une entente sur un marché de "
        "200&nbsp;M&nbsp;€ prend un risque professionnel majeur et apporte ce "
        "qu'aucun contrôle de routine ne trouvera. Un voisin qui signale un "
        "allocataire n'apporte rien que la caisse ne puisse vérifier "
        "elle-même, et coûte davantage qu'il ne rapporte.</p>"
        "<p>Trois garde-fous&nbsp;: la décision appartient à une autorité "
        "indépendante et non à l'administration bénéficiaire&nbsp;; la prime "
        "est versée sur les sommes <b>effectivement encaissées</b>, ce qui "
        "élimine le signalement spéculatif&nbsp;; le barème est public, donc "
        "contestable.</p>"
        "<p>Et la contrepartie est réelle&nbsp;: la France protège aujourd'hui "
        "les lanceurs d'alerte contre les représailles, mais ne compense "
        "rien. Perdre son emploi et cinq ans de sa vie pour avoir eu raison "
        "reste le parcours type.</p>",
        "",
        "delation",
    )

    corps += cle(
        "« L'indépendance du parquet exige le Congrès : vous promettez ce que "
        "personne n'a jamais obtenu »",
        "C'est vrai, et nous ne le cachons pas&nbsp;: la révision a été votée "
        "par les deux assemblées puis abandonnée avant le Congrès en 2019. "
        "<b>La mesure comporte donc une partie qui ne dépend pas de lui.</b>",
        "<p>Par la loi ordinaire, dès la première année&nbsp;: publication de "
        "toutes les nominations du parquet, de l'avis du Conseil supérieur de "
        "la magistrature et, lorsque le garde des Sceaux s'en écarte, des "
        "motifs pour lesquels il s'en écarte. On ne retire pas le pouvoir de "
        "nommer&nbsp;; on rend son exercice visible, et l'expérience montre "
        "qu'un pouvoir discrétionnaire qui doit se motiver publiquement "
        "s'exerce autrement.</p>"
        "<p>La révision constitutionnelle reste l'objectif, parce qu'elle "
        "seule règle la question. Mais un programme qui ferait dépendre sa "
        "crédibilité d'un vote aux trois cinquièmes serait un programme "
        "suspendu.</p>",
        "",
        "congres",
    )

    corps += cle(
        "« Vous citez l'Ukraine, l'un des pays les plus corrompus d'Europe, "
        "comme modèle anticorruption »",
        "Oui — et c'est exactement pour cela que l'exemple vaut. <b>Un "
        "dispositif qui produit un effet mesurable dans un environnement "
        "hostile en produira un ici.</b>",
        "<p>L'argument inverse serait de citer le Danemark&nbsp;: on ne "
        "saurait jamais si le résultat vient de la plateforme ou du pays. "
        "<i>Prozorro</i> a été mis en place dans un État où la commande "
        "publique était notoirement captée, et l'effet observé — baisse des "
        "prix d'attribution, hausse du nombre de soumissionnaires — est "
        "attribuable à la publication elle-même, parce que rien d'autre "
        "n'avait changé.</p>"
        "<p>Nous citons aussi <i>USAspending</i> aux États-Unis et le "
        "<i>tax gap</i> britannique, qui sont des environnements tout autres. "
        "Le point commun des trois n'est pas le pays&nbsp;: c'est qu'une "
        "donnée publiée en format ouvert change le comportement de ceux qui "
        "savent qu'elle sera lue.</p>",
        "",
        "ukraine",
    )

    corps += cle(
        "« Un parti qui réclame la transparence de l'argent public ferait "
        "mieux de commencer par le sien »",
        "<b>L'objection porte, et elle a produit la mesure n°&nbsp;6.</b> "
        "Elle ne figurait pas dans la première version de ce programme, et "
        "son absence était le trou le plus visible.",
        "<p>La mesure demande la publication en données ouvertes des comptes "
        "de campagne et des comptes des partis, des frais de mandat poste par "
        "poste, et des moyens réels de contrôle pour la Commission nationale "
        "des comptes de campagne. Elle s'applique à nous exactement comme aux "
        "autres.</p>"
        "<p>Nous ne demandons pas qu'on nous croie sur parole&nbsp;: le code "
        "de ce site, son historique de corrections et les hypothèses de son "
        "chiffrage sont publics depuis le premier jour. C'est un début, et "
        "ce n'est pas suffisant.</p>",
        "Voir la mesure n°&nbsp;6 sur "
        "<a href=\"programme.html#exposer\">Programme</a>.",
        "nous",
    )

    corps += depliant(
        "Trois objections plus courtes, et leurs réponses",
        "<p><b>« Vos chiffres datent. »</b> L'objection a porté, et elle a "
        "été traitée&nbsp;: contrôle fiscal 2025, indice de perception 2025, "
        "non-recours au RSA publié en mai&nbsp;2026, commande publique 2024, "
        "comptes publics 2025, dépenses fiscales du budget pour 2026. Deux "
        "chiffres restent vieux et nous les gardons faute de mieux&nbsp;: "
        "l'estimation du Conseil des prélèvements obligatoires (2007) et "
        "l'étude de l'Insee sur la TVA (portant sur 2012). Leur ancienneté "
        "n'est pas un défaut de ce site&nbsp;; <b>c'est le sujet de ce "
        "site</b>. La liste complète des millésimes est sur "
        "<a href=\"sources.html\">Sources</a>, et un retard se signale sur "
        "le dépôt.</p>"
        "<p><b>« Vous ne créez aucune agence, mais vous ajoutez 2 000 "
        "agents. »</b> Les deux sont compatibles, et c'est le cœur de notre "
        "position&nbsp;: la France n'a pas besoin d'une quinzième institution, "
        "elle a besoin que les quatorze existantes aient les effectifs, les "
        "données et l'indépendance qui leur manquent. L'AFA compte une "
        "cinquantaine d'agents, le parquet national financier une vingtaine "
        "de magistrats.</p>"
        "<p><b>« L'exclusion des marchés après une convention judiciaire "
        "viole la présomption d'innocence. »</b> Elle la violerait si elle "
        "était automatique, la convention étant sans reconnaissance de "
        "culpabilité. C'est pourquoi nous proposons l'inverse&nbsp;: faire de "
        "l'exclusion et de sa durée un <b>terme négocié de la convention "
        "elle-même</b>, homologué par le juge qui la valide. L'entreprise "
        "sait ce qu'elle signe.</p>",
    )

    corps += vigilance(
        "<b>Quatre des objections ci-dessus portent</b>, et nous l'écrivons à "
        "l'endroit où on les lira&nbsp;: nous ne savons pas quelle fraction "
        "du problème ce programme traite tant que l'écart fiscal n'est pas "
        "publié&nbsp;; la neutralité de la réforme fiscale vaut en masse et "
        "non pour chaque contribuable&nbsp;; et notre première version "
        "soutenait sur le niveau des prélèvements une thèse que la "
        "littérature ne soutient pas, ce qui nous a valu de réécrire une "
        "page&nbsp;; et notre estimation du rendement de la publication des "
        "marchés repose sur une assiette qui a elle-même bougé de 160 à "
        "233&nbsp;Md&nbsp;€ en un exercice, pour une raison de mesure et non "
        "de dépense. Les corrections sont dans l'historique du dépôt, à la "
        "vue de tous."
    )

    return page(
        "objections.html",
        "Objections — ce qu'on nous oppose, et ce que nous répondons",
        "Les neuf objections les plus solides faites à ce programme, dans "
        "leur version la plus forte, et nos réponses — y compris les quatre "
        "qui portent.",
        corps,
    )


# ---------------------------------------------------------------------------
# 8. Sources — tout ce qui est cité, avec le lien et la date
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
  <p>Les <b>millésimes</b> repris ici sont les plus récents publiés par chaque
  source à la date de notre dernière revue&nbsp;: contrôle fiscal 2025 (DGFiP),
  fraude sociale 2025 et travail dissimulé décembre 2024 (HCFiPS), non-recours
  au RSA mai 2026 (DREES), indice de perception 2025 (Transparency
  International), commande publique 2024 (OECP), comptes publics 2025 (Insee),
  dépenses fiscales du projet de loi de finances pour 2026, condamnations pour
  atteinte à la probité 2016-2022 (AFA) et estimation du Conseil des
  prélèvements obligatoires de 2007 — faute de plus récente. Quand une source
  publie un millésime plus neuf et que ce site ne l'a pas repris, <b>c'est un
  défaut</b>&nbsp;: il se signale sur le dépôt et se corrige.</p>
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
            ("<b>Cour des comptes</b>, <i>La lutte contre la fraude "
             "fiscale</i>, rapport public thématique, 16&nbsp;décembre&nbsp;2025",
             "La référence la plus récente et la plus complète. Elle "
             "établit&nbsp;: l'absence d'estimation de l'écart fiscal et le "
             "refus d'arbitrer entre les chiffres en circulation&nbsp;; le "
             "recul du rendement du contrôle rapporté aux recettes fiscales, "
             "de 4,3&nbsp;% (2015) à 2,8&nbsp;% (2024)&nbsp;; la baisse de "
             "19&nbsp;% des effectifs du contrôle entre 2015 et 2024&nbsp;; "
             "le reflux des poursuites pénales (plus de 850 par an avant 2018, "
             "≈ 700 en 2023-2024) et du taux de sanction (30&nbsp;% de "
             "l'impôt éludé en 2015, 15&nbsp;% dix ans plus tard).",
             _lien("ccomptes.fr — La lutte contre la fraude fiscale",
                   "https://www.ccomptes.fr/fr/publications/la-lutte-contre-la-fraude-fiscale")),
            ("DGFiP",
             "Rapports d'activité et communiqués annuels&nbsp;: montants "
             "notifiés et encaissés, nombre de contrôles. Millésime 2025 "
             "retenu ici&nbsp;: 17,1&nbsp;Md&nbsp;€ notifiés, "
             "11,4&nbsp;Md&nbsp;€ encaissés. Travaux préliminaires de 2024 sur "
             "l'écart de TVA déclarée&nbsp;: 6 à 10&nbsp;Md&nbsp;€.",
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
             "la fraude. Édition de décembre&nbsp;2025, portant sur "
             "2023&nbsp;: 128&nbsp;Md&nbsp;€ pour l'Union. Dernier chiffre "
             "français que nous ayons pu vérifier&nbsp;: 9,6&nbsp;Md&nbsp;€ "
             "et 4,9&nbsp;% des recettes pour 2021.",
             _lien("taxation-customs.ec.europa.eu — TVA",
                   "https://taxation-customs.ec.europa.eu/taxation/vat_en")),
            ("Solidaires Finances Publiques",
             "Estimation syndicale de 80 à 100&nbsp;Md&nbsp;€ (2019), la plus "
             "citée dans le débat public et jamais reprise par l'État.",
             _lien("solidairesfinancespubliques.org",
                   "https://solidairesfinancespubliques.org/")),
            ("HM Revenue &amp; Customs (Royaume-Uni)",
             "<i>Measuring tax gaps</i>&nbsp;: la série annuelle de référence, "
             "publiée depuis 2005. C'est le modèle de notre mesure n°&nbsp;8.",
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
             "Note annuelle de suivi et d'évaluation des fraudes "
             "sociales&nbsp;: ≈ 14&nbsp;Md&nbsp;€ estimés pour 2025, "
             "17,5&nbsp;Md&nbsp;€ en y ajoutant les erreurs de bonne foi. "
             "Observatoire du travail dissimulé (décembre&nbsp;2024)&nbsp;: "
             "6 à 7,8&nbsp;Md&nbsp;€ par an pour les salariés du privé non "
             "agricole.",
             _lien("strategie-plan.gouv.fr — HCFiPS",
                   "https://www.strategie-plan.gouv.fr/")),
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
             "<i>Études et résultats</i> n°&nbsp;1370, mai&nbsp;2026&nbsp;: "
             "33 à 37&nbsp;% des foyers éligibles au RSA ne le percevaient "
             "pas fin 2021, soit ≈ 560&nbsp;000 foyers et près d'un million "
             "de personnes.",
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
             "France, millésimes 2019 à 2025 — 66/100 et 27ᵉ sur 182 en 2025. "
             "Mesure une perception par des experts et des milieux "
             "d'affaires, pas un nombre d'actes&nbsp;; l'organisation "
             "recommande de comparer les notes et non les rangs.",
             _lien("transparency.org — CPI 2025",
                   "https://www.transparency.org/en/cpi/2025")),
            ("GRECO — Conseil de l'Europe",
             "Rapports d'évaluation et de conformité sur la France, "
             "notamment le cinquième cycle (hautes fonctions de l'exécutif et "
             "services répressifs).",
             _lien("coe.int — GRECO", "https://www.coe.int/fr/web/greco")),
            ("Agence française anticorruption",
             "Rapports annuels, recommandations, suivi des CJIP, et analyse "
             "des condamnations pénales pour atteinte à la probité portant "
             "sur 2016-2022&nbsp;: ≈ 3&nbsp;000 infractions sanctionnées sur "
             "la période, soit de l'ordre de 400 par an, dont 502 pour la "
             "seule année 2022.",
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
             "Recensement annuel des marchés publics. Millésime 2024&nbsp;: "
             "233,3&nbsp;Md&nbsp;€ pour 223&nbsp;383 marchés, dont "
             "100,7&nbsp;Md&nbsp;€ pour le secteur public local. Le bond par "
             "rapport aux exercices précédents tient pour l'essentiel à "
             "l'abaissement du seuil de déclaration obligatoire de "
             "90&nbsp;000 à 40&nbsp;000&nbsp;€&nbsp;: c'est la mesure qui a "
             "changé, pas l'achat.",
             _lien("economie.gouv.fr — DAJ",
                   "https://www.economie.gouv.fr/daj")),
            ("Insee",
             "<i>Le compte des administrations publiques en 2025</i>&nbsp;: "
             "dépense publique de 1&nbsp;714,2&nbsp;Md&nbsp;€, soit "
             "57,3&nbsp;% du PIB&nbsp;; taux de prélèvements obligatoires de "
             "43,6&nbsp;% du PIB, net des crédits d'impôt.",
             _lien("insee.fr", "https://www.insee.fr/")),
            ("Eurostat",
             "Comparaison européenne du taux de prélèvements obligatoires. "
             "<b>Attention au périmètre&nbsp;:</b> Eurostat inclut les "
             "cotisations sociales imputées et ne déduit pas les crédits "
             "d'impôt, d'où 45,3&nbsp;% du PIB pour la France en 2024 quand "
             "l'Insee retient 42,7&nbsp;%. Sur la définition d'Eurostat, la "
             "France est <b>deuxième</b> de l'Union, derrière le Danemark "
             "(45,8&nbsp;%) et devant la Belgique (45,1&nbsp;%).",
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
            ("Directive (UE) 2021/2101 du 24 novembre 2021",
             "Publication par les grands groupes des informations relatives à "
             "l'impôt sur les bénéfices, pays par pays. Le fondement de la "
             "seconde moitié de notre mesure n°&nbsp;5."),
            ("Règlement (UE) 2024/1624 et directive (UE) 2024/1640 du "
             "31 mai 2024 (paquet anti-blanchiment)",
             "Réorganisent le cadre européen et rouvrent les registres de "
             "bénéficiaires effectifs aux porteurs d'un intérêt légitime. La "
             "transposition générale court jusqu'au 10&nbsp;juillet&nbsp;2027, "
             "<b>mais les articles 11 à 13 et 15, qui portent précisément sur "
             "ces registres, devaient l'être au 10&nbsp;juillet&nbsp;2026</b> "
             "— échéance dépassée."),
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
             "fraude&nbsp;: gain attendu, probabilité de détection, sanction. "
             "Attention&nbsp;: il ne conclut pas de façon univoque sur l'effet "
             "du <i>niveau</i> du taux, contrairement à ce que nous avons "
             "d'abord écrit."),
            ("Yitzhaki S., <i>A note on income tax evasion: a theoretical "
             "analysis</i>, Journal of Public Economics, 1974",
             "Corrige le précédent&nbsp;: lorsque la pénalité est "
             "proportionnelle à l'impôt éludé — le cas français —, une hausse "
             "du taux peut <i>réduire</i> la fraude. C'est l'objection qui "
             "nous a fait réécrire la cause n°&nbsp;2 du diagnostic."),
            ("Kleven H. et al., <i>Unwilling or unable to cheat?</i>, "
             "Econometrica, 2011",
             "L'expérience danoise à grande échelle qui établit le résultat "
             "central de notre diagnostic&nbsp;: la fraude est quasi nulle sur "
             "les revenus déclarés par un tiers, massive sur les revenus "
             "auto-déclarés."),
            ("<i>SEC Whistleblower Program</i> (États-Unis, depuis 2011)",
             "Récompense de 10 à 30&nbsp;% des sanctions supérieures à un "
             "million de dollars&nbsp;; modèle de notre mesure n°&nbsp;10. Voir "
             + _lien("sec.gov/whistleblower",
                     "https://www.sec.gov/whistleblower") + "."),
        ),
        ("long", "long"),
    )

    corps += '<h2 id="hypotheses" tabindex="-1">Nos hypothèses de chiffrage</h2>'
    corps += """
<p>Tout le reste de ce site reprend des chiffres publics. La page
<a href="chiffrage.html">Chiffrage</a>, elle, ne le peut pas entièrement&nbsp;:
estimer le coût et le rendement de mesures qui n'existent pas encore suppose
des hypothèses, et ces hypothèses sont de nous. Les voici, isolées et nommées,
<b>pour qu'on puisse les contester une par une</b>.</p>
"""
    corps += tableau(
        "Les six hypothèses qui ne viennent pas d'une source publique",
        ("Hypothèse", "Valeur retenue", "Sur quoi elle s'appuie"),
        (
            ("Coût complet employeur d'un agent",
             "80 à 110 k&nbsp;€/an",
             "Rémunération chargée, fonctions support et immobilier, pour des "
             "corps de catégorie A et des magistrats&nbsp;; ordres de grandeur "
             "des rapports annuels de performances et du jaune budgétaire "
             "consacré à la fonction publique."),
            ("Effectifs supplémentaires",
             "≈ 2&nbsp;000 ETP",
             "<b>C'est une décision politique, pas une donnée.</b> Ils "
             "viennent en sus des 1&nbsp;500 agents du plan de 2023, et ne "
             "rattrapent pas la baisse d'environ un quart observée dans les "
             "années 2010."),
            ("Refonte des systèmes d'information des caisses",
             "150 à 400 M&nbsp;€ sur cinq ans",
             "Ordre de grandeur du chantier du prélèvement à la source "
             "(2019), à périmètre comparable."),
            ("Portail unique de la dépense publique",
             "20 à 50 M&nbsp;€/an",
             "Coûts publiés de plateformes de données publiques comparables, "
             "en réutilisant des briques existantes plutôt qu'en repartant de "
             "zéro."),
            ("Effet de la publication des marchés",
             "− 0,3 à − 1,9&nbsp;% sur 233&nbsp;Md&nbsp;€",
             "Travaux sur <i>Prozorro</i> et sur l'ouverture des enchères "
             "publiques, appliqués au montant recensé par l'OECP en 2024. "
             "C'est notre hypothèse la plus incertaine&nbsp;; la fourchette "
             "est large pour cette raison."),
            ("Part encaissée visée",
             "80 % des montants notifiés",
             "Niveau atteint en 2019 et en 2021 (DGFiP). Nous le retenons "
             "comme cible parce qu'il a déjà été observé, et non comme un "
             "progrès inédit&nbsp;— la part est retombée à 67&nbsp;% en 2025."),
        ),
        ("texte", "nombre", "long"),
    )
    corps += """
<p class="discret">Ces six lignes sont les seules du site qui ne sont pas
reprises d'une source extérieure. Si l'une d'elles vous paraît fausse, le
chiffrage entier bouge&nbsp;: c'est exactement pour cela qu'elles sont
écrites ici plutôt que fondues dans un total.</p>
"""

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
