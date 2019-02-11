# import markdown
import markdown2
import codecs
import black
import argparse
import random
from pathlib import Path



# Création des commandes
give = argparse.ArgumentParser()

give.add_argument("-i","--input", "--input-directory", type = str, help = "Chemin du dossier de fichiers source (contenant les fichiers markdown)")
give.add_argument("-o","--output", "--output-directory", type = str, help = "Chemin du dossier où seront mis les fichiers générés pour le site statique")

# A faire
give.add_argument("-t", "--title", type = str, help = "Mettre un titre sur le fichier HTML")
argument1 = give.parse_args()

if argument1.input != None:
    insideMD = argument1.input
    insideMD = insideMD + "/"
else:
    insideMD = "./Markdown/"
    pass

if argument1.output != None:
    insideSITE = argument1.output
else:
    insideSITE = "./Site_Statique/"
    pass


#Fonction qui convertie le Markdown en HTML
def convert_MD_to_HTML(insideMD, le_sorted, page):
    action = False

    # Vérification qu'il y est bien un fichier à convertir et qu'il soit de la bonne syntax
    if insideMD != None and insideMD != "./Markdown/Mardown_1.md":
        fich = insideMD + "Markdown_1.md"
    else:
        pass

    if page > 1:
        fich = "./Markdown/" + le_sorted[page-1].name
    
    print(fich)
    #Création du fichier new_md vide
    new_md = codecs.open(fich, mode='r', encoding="UTF-8")
    text = new_md.read()
    #Utilisation de markdown 2 pour convertir le fichier texte(MD) en html
    html = markdown2.markdown(text)

    #Ouverture du template Body du html + écriture du fichier convertie en MD dedans
    fichier = open("./template/second_html.html", "w")
    fichier.write(html)
    fichier.close

    fichier = open("./template/second_html.html", "r")
    #Création du fichier set pour avoir les bonne tabulation
    fichier_set = open("./template/set.html", "w")

    # Boucle permetant de mettre les tabulation
    for l in fichier:
        if action == False:
            fichier_set.write('\t\t')
            action = True
        fichier_set.write(l.replace('\n', '\n\t\t'))
    
    fichier.close()


def creat_CSS():

    fichier = open("./Site_Statique/style.css", "w")
    fichier = open("./Site_Statique/style.css", "a")
    css = codecs.open("./template/style.css", mode="r", encoding="UTF-8")
    thecss = css.read()

    fichier.write(thecss)


def DUTCH():
    fichiergo = open("./Site_Statique/indexall.html", "w")
    fichiergo = open("./Site_Statique/indexall.html", "w")
    fichierall = codecs.open("./Site_Statique/index.html", mode="r", encoding="UTF-8")
    fichieridk = fichierall.read()

    fichieridk.replace("qu", "k")
    fichierall.replace("ce", "ze")
    fichierall.replace("ç", "z")
    fichierall.replace("gu", "ch")
    fichierall.replace("g", "ch")
    fichierall.replace("j", "k")
    fichierall.replace("v", "f")

    fichiergo.write(fichierall)

    

# Fonction qui fusione les 2 fichiers HTML Template + le nouveau Body
def creat_HTML(insideSITE, page):
    compteur = str(page)


    if insideSITE != None and insideSITE != "./Site_Statique/index.html":
        site = insideSITE + "./index.html"
    else:
        pass
    
    if page > 1:
        site = "./Site_Statique/page" + compteur + ".html"
    
    fichier = open(site, "w")
    fichier = open(site, "a")

    # ça ecrit dans la première partie dans le fichier
    first_html = codecs.open("./template/first_html.html", mode="r", encoding="UTF-8")
    firsthtml = first_html.read()
    fichier.write(firsthtml)

    # ça ecrit le body dans le fichier avec les tabulation(fichier set)
    sechtml = codecs.open("./template/set.html", mode="r", encoding="UTF-8")
    lehtml = sechtml.read()
    fichier.write(lehtml)

    # ça écrit la fin du html dans le fichier
    troihtml = codecs.open("./template/3_html.html", mode="r", encoding="UTF-8")
    troishtml = troihtml.read()
    fichier.write(troishtml)

#LA GODFUNCTION sert à utiliser les trois autres fonction + boucle while si on à plusieur fichiers
def GODFUCTION(insideMD, insideSITE, le_sorted, compteurMD):
    page = 1
    while page != compteurMD+1:
        convert_MD_to_HTML(insideMD,le_sorted,page)
        creat_HTML(insideSITE,page)
        page += page
    creat_CSS()
    #DUTCH()
    print('Conversion successful!')



le_sorted = sorted(Path(insideMD).glob('*.md'))
compteurMD = len(le_sorted)
GODFUCTION(insideMD,insideSITE,le_sorted,compteurMD)











