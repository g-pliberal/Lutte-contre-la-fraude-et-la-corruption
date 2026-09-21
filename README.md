# Lutte contre la fraude et la corruption

Le site du **Parti libéral français** sur la fraude et la corruption : ce que la
France fait aujourd'hui, ce que cela donne, et l'alternative libérale que nous
proposons.

Sept pages, statiques, sans serveur, sans script côté client, sans requête vers
un tiers — polices comprises. On ouvre `index.html` dans un navigateur et le
site est là.

## Ce que le site dit

| Page | Ce qu'on y trouve |
| --- | --- |
| `index.html` | L'affiche, les quatre engagements, la méthode en trois gestes |
| `constat.html` | Les estimations publiques de la fraude fiscale, sociale et de la corruption — avec leurs contradictions |
| `dispositif.html` | La politique actuelle : onze lois depuis 1993, quatorze institutions, leurs moyens réels |
| `diagnostic.html` | Pourquoi ce dispositif plafonne, en sept causes |
| `programme.html` | Les dix mesures, en trois blocs — assécher, exposer, sanctionner |
| `chiffrage.html` | Ce que cela coûte, ce que cela peut rapporter, et notre degré de confiance ligne à ligne |
| `sources.html` | Toutes les sources citées, avec leur date et le lien pour les vérifier |

## Les règles d'écriture

Elles ne sont pas décoratives : c'est un site qui réclame la transparence de
l'État, il se doit d'être vérifiable lui-même.

1. **Aucun chiffre n'est de nous.** Chacun a une source publique, une date et un
   périmètre, listés dans `sources.html`.
2. **Quand deux sources officielles se contredisent, on donne les deux** et on
   dit que l'État n'arbitre pas. C'est précisément l'argument du site.
3. **On distingue trois choses** que le débat public confond : un montant
   *estimé*, un montant *détecté*, un montant *encaissé*.
4. **On ne promet pas de rendement précis** sur une assiette que personne ne
   sait mesurer. Le chiffrage donne des fourchettes et affiche son degré de
   confiance, y compris quand il est faible.
5. **Ce que nous refusons est écrit** au même endroit que ce que nous proposons
   (`programme.html`, section « Ce que nous refusons »).

## Construire

Les pages sont **générées puis versionnées** : le dépôt contient le HTML servi,
et le script qui l'écrit. La raison est simple — le bandeau, le pied et l'affiche
ne doivent exister qu'à un seul endroit ; un onglet ajouté à la main sur six
pages sur sept est un onglet manquant.

```sh
python3 scripts/construire.py   # réécrit les sept pages à la racine
python3 scripts/verifier.py     # les vérifie
```

Aucune dépendance : Python 3.10 ou plus récent, bibliothèque standard seulement.

`verifier.py` contrôle cinq choses, qui sont exactement les erreurs qu'on ne
voit pas en relisant :

- le balisage est équilibré ;
- tout lien interne mène quelque part — fichier **et** ancre, y compris d'une
  page à l'autre ;
- chaque page a son onglet actif, et un seul, et un `<h1>`, un seul ;
- toute classe écrite dans le HTML existe dans la feuille de style (une faute
  de frappe dans un nom de classe est un bloc sans style, et rien ne le
  signale) ;
- aucune entité HTML n'a été échappée deux fois.

**À relancer après toute modification de `scripts/`**, et à commiter avec elle.

## Organisation

```
index.html … sources.html   les pages servies (générées — ne pas éditer à la main)
ressources/style.css        la feuille de style, seul point de vérité de la charte
ressources/polices/         Public Sans et Instrument Serif, servies par le dépôt (OFL)
ressources/icone.svg        l'icône du site
scripts/gabarit.py          ce qui est le même sur toutes les pages
scripts/pages.py            le contenu, une fonction par page
scripts/construire.py       écrit les pages
scripts/verifier.py         les vérifie
```

## La charte

Elle est **celle du site [Retraite à comptes notionnels](https://github.com/g-pliberal/retraitecomptenotionelle)** :
même vert profond, même or, mêmes deux polices, mêmes noms de variables CSS. Les
deux sites sont des outils du même parti, et un électeur qui passe de l'un à
l'autre doit reconnaître la maison.

Un seul thème, et c'est voulu : l'affiche *est* l'identité, la décliner en clair
donnerait deux sites qui ne disent pas la même chose. Les contrastes sont
mesurés et tiennent le plancher de 4,5:1 même pour le petit texte ; rien n'est
signalé par la seule couleur.

Les polices sont **servies par le dépôt et non par un tiers** : une requête de
police chez un hébergeur extérieur emporte l'adresse IP du lecteur, et un site
qui parle de transparence n'a pas à en prendre l'habitude.

## Une erreur ?

Si un chiffre vous paraît faux, obsolète ou sorti de son contexte, ouvrez un
signalement. Il sera corrigé, et la correction sera visible dans l'historique.

## Licences

- Code du site (`scripts/`, `ressources/style.css`) : **Apache 2.0**, voir `LICENSE`.
- Textes et infographies : **CC BY-SA 4.0**.
- Polices Public Sans et Instrument Serif : **SIL Open Font License 1.1**, voir
  `ressources/polices/`.
