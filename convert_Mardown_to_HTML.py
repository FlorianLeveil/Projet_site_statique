# import markdown
import markdown2
import codecs
import argparse
import random
from pathlib import Path


# Création des commandes
give = argparse.ArgumentParser()

give.add_argument("-i", "--input-directory", type = str, help = "Chemin du dossier de fichiers source (contenant les fichiers markdown)")
give.add_argument("-o", "--output-directory", type = str, help = "Chemin du dossier où seront mis les fichiers générés pour le site statique")
give.add_argument("-t", "--title", type = str, help = "Mettre un titre sur le fichier HTML")


argument = give.parse_args()

if argument.input != None:
    insideMD = argument.input
    insideMD = give + "/"

else:
    insideMD = "./Markdown/"
    pass

if argument.output != None:
    insideSITE = argument.output

else:
    insideSITE = "./Site_Statique/"
    pass

def convert_MD_to_HTML(insideMD, le_sorted, page):
    action = False

    # Vérification qu'il y est bien un fichier à convertir et qu'il soit de la bonne syntax
    if insideMD != None and insideMD != "./Markdown/Mardown_1.md":
        fich = insideMD + "Markdown_1.md"
    else:
        pass

    if page > 1:
        fich = "./Markdown/" + le_sorted[page-1]
    
    #Création du fichier new_md vide
    new_md = codecs.open(fich, mode='r', encoding="UTF-8")
    text = new_md.read()
    #Utilisation de markdown 2 pour convertir le fichier texte(MD) en html
    html = markdown2.markdown(text)


    fichier = open("./template/index.html")
    fichier.write(html)
    fichier.close

    fichier = open("./template/index.html", "r")
    fichier_set = open("./template/page.html", "w")

    for l in fichier:
        if action == False:
            fichier_set.write('\t')
            action = True
        fichier_set.write(ligne.replace('\n', '\n\t'))
    
    fichier.close()

def creat_HTML(insideMD, page):
    compteur = str(page)

    if insideSITE != None and insideSITE != "./Site_Statique/index.html":
        site = insideSITE + "./index.html"
    else:
        pass
    
    if page > 1:
        site = "./Site_Statique/page" + compteur + ".html"
    
    fichier = open(site, "w")
    fichier = open(site, "a")

    html = codecs.open("./template/index.html", mode="r", encoding="UTF-8")
    lehtml = html.read()

    fichier.write(lehtml)

def creat_CSS():

    fichier = open("./Site_Statique/Cstyle.css", "w")
    fichier = open("./Site_Statique/style.css", "a")
    css = codecs.open("./template/style.css", mode="r", encoding="UTF-8")
    txtcss = css.read()

    fichier.write(txtcss)

def GODFUCTION(insideMD, insideSITE, le_sorted, compteurMD):
    page = 1
    while page != compteurMD:
        convert_MD_to_HTML(insideMD,le_sorted,page)
        creat_HTML(insideSITE,page)
        page += page
    creat_CSS()

le_sorted = sorted(Path(insideMD).glob('*.md'))
compteurMD = len(le_sorted)

GODFUCTION(insideMD,insideSITE,le_sorted,compteurMD)











