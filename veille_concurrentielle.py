# Les exigences du système de surveillance
# des prix
# Ce document contient les exigences et les instructions pour élaborer une version
# bêta du système de surveillance des prix pour Books Online.
# Notes:
# ● Au cours du projet, veillez à enregistrer votre code dans un repository
# GitHub et à effectuer des commits réguliers accompagnés de messages de
# commit clairs.
# ● N'oubliez pas que vous devez enregistrer un fichier requirements.txt sans
# enregistrer votre environnement virtuel dans le repository lui-même.
# ● Vous ne devez pas non plus enregistrer vos fichiers CSV.
# ● Veillez également à prendre le temps d'écrire un fichier README.md, que
# vous ajouterez dans le repository afin que je puisse exécuter le code
# correctement et produire quelques données !



# Phase 1

# Choisissez n'importe quelle page Produit sur le site de Books to Scrape. Écrivez un
# script Python qui visite cette page et en extrait les informations suivantes :
# ● product_page_url
# ● universal_ product_code (upc)
# ● title
# ● price_including_tax
# ● price_excluding_tax
# ● number_available
# ● product_description
# ● category
# ● review_rating
# ● image_url
# Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme
# en-têtes de colonnes.

# Phase 2
# Maintenant que vous avez obtenu les informations concernant un premier livre,
# vous pouvez essayer de récupérer toutes les données nécessaires pour toute une
# catégorie d'ouvrages.
# Choisissez n'importe quelle catégorie sur le site de Books to Scrape. Écrivez un
# script Python qui consulte la page de la catégorie choisie, et extrait l'URL de la
# page Produit de chaque livre appartenant à cette catégorie.
# Combinez cela avec le travail que vous avez déjà effectué dans la phase 1 afin
# d'extraire les données produit de tous les livres de la catégorie choisie, puis écrivez
# les données dans un seul fichier CSV.
# Remarque : certaines pages de catégorie comptent plus de 20 livres, qui sont
# donc répartis sur différentes pages (« pagination »). Votre application doit être
# capable de parcourir automatiquement les multiples pages si présentes.
# Phase 3
# Ensuite, étendez votre travail à l'écriture d'un script qui consulte le site de Books
# to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les
# informations produit de tous les livres appartenant à toutes les différentes
# catégories. Vous devrez écrire les données dans un fichier CSV distinct pour
# chaque catégorie de livres.
# Phase 4
# Enfin, prolongez votre travail existant pour télécharger et enregistrer le fichier
# image de chaque page Produit que vous consultez.


import requests
from bs4 import BeautifulSoup
#Phase 1) 
# preparer le tableau
veille_concurrentielle = [("product_page_url","universal_product_code (upc)", "title","price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url")]

def retourner_la_cle_de_la_liste_a_partir_de_la_colonne_de_gauche(colonne_de_gauche):
    # match colonne_de_gauche:
    #     case "UPC": 
    #         return 1
    #     case "Price (incl. tax)":
    #         return 3
    #     case "Price (excl. tax)":
    #         return 4
    #     case "Availability":
    #         return 5
    #     case _: 
    #         return Nonegti
    if colonne_de_gauche == "UPC": 
        return 1
    elif colonne_de_gauche == "Price (incl. tax)":
        return 3
    elif colonne_de_gauche == "Price (excl. tax)":
        return 4
    elif colonne_de_gauche == "Availability":
        return 5
    else : 
        return None

# recupérer la page
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

r = requests.get(url)


if r.ok:
# vérifier que la page est bien


    ligne = ["missing"] * len(veille_concurrentielle[0])
#parcer
    soup = BeautifulSoup(r.text, 'html.parser')

#Recuperer  
# ● product_page_url
    ligne[0] = url


    #trs = soup.find_all("tr")
    #title = soup.find("h1").get_text()
    #for tr in trs: 
        #match tr.find("th").get_text():
            #case "UPC":
            #    universal_product_code = tr.find("td").get_text()
           # case "Price (excl. tax)":
            #    price_excluding_tax = tr.find("td").get_text()[1:]
        
    #print(universal_product_code, price_excluding_tax)
    #print(title)
        

# ● title
    ligne[2] = soup.find("h1").get_text()


# ● universal_ product_code (upc)
# ● price_including_tax
# ● price_excluding_tax
# ● number_available
    trs = soup.find_all("tr")
    
 
    for tr in trs:
        text_colonne_de_gauche = tr.find("th").get_text()
        cle = retourner_la_cle_de_la_liste_a_partir_de_la_colonne_de_gauche(text_colonne_de_gauche)
        if cle == None:
            continue
        colonne_de_droite = tr.find("td").get_text()
        if cle == 5:
            colonne_de_droite = colonne_de_droite.replace("In stock (", "").replace(" available)","")
        if cle == 4 or cle == 3:
            colonne_de_droite = colonne_de_droite[1:]
        ligne[cle] = colonne_de_droite
        
        


# ● product_description

# ● category

# ● review_rating

# ● image_url


    veille_concurrentielle.append(ligne)
# Si la page est pas ok 

 
# Resultat de la phase 1) ==>creeer un csv 
#   Que faire pour arriver a ca ? ==> 
#   Comment les stocker ? ==> Cs
#   
# Result

for line in veille_concurrentielle:
    print(line)

# ---- FAIRE script p
