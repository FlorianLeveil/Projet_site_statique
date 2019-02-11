# Site Statique
## Résumé:

Le script Convert_MD_to_HTML sert à convertir un fichier (ou plusieurs) Markdown en un fichier HTML + un fichier CSS.

## Setup:

* Un IDE de vôtre choix
* Installation des librairies:
	 * `pip install python`
	 * `pip install mardown2`
	 * `pip install coreapi`
	 * `pip install argparse`
* Cloner mon git: `git clone https://github.com/FlorianLeveil/Projet_site_statique`

## Utilisation:
1. Ouvrir un terminal.
2. Aller dans le dossier cloné.
```
PS A:\Ynov\Projet_site_statique> ls
Répertoire : A:\Ynov\Projet_site_statique

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/02/2019     15:53                Markdown
d-----       11/02/2019     19:21                Site_Statique
d-----       11/02/2019     15:11                template
-a----       11/02/2019     20:56           4759 convert_Mardown_to_HTML.py
-a----       09/02/2019     19:35             22 README.md
```
3. Nommez vos/vôtre fichier(s) `Markdown_1`, `Markdown_2`, ect...
4. Mettez vos/vôtre fichier(s) dans le dossier Makrdown
5. Taper dans la console `python .\convert_Mardown_to_HTML.py`
6. Vos/vôtre fichier(s) Makrdown sont/est dans le dossier Site_Statique

## Arguments possible:
Si vous voulez changer le dossier d'importation vous pouvez utilisé l'argument `-i`
* Exemple:
```
python .\convert_Mardown_to_HTML.py -i Mon_autre_dossier
```

Si vous voulez changer le dossier de destination vous pouvez utilisé l'argument `-o`
* Exemple:
```
python .\convert_Mardown_to_HTML.py -o Mon_autre_dossier
```

## Bonus:

En plus du fichier convertie en HTML vous trouverez un fichier indexall.html.
Ce fichier est la conversion du fichier index.html en pseudo allemand .