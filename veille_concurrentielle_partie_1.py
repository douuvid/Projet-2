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
from bs4 import BeautifulSoup # Pour filtres les balises
import csv

# Parser ==> extraire de la donne a parir du texte

nombres = {
    "Zero": 0,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

    
#Phase 1) 
# preparer le tableau
veille_concurrentielle = [("product_page_url","universal_product_code (upc)", "title","price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url")]


# recupérer la page
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

r = requests.get(url)



if r.ok:
# vérifier que la page est bien


#parcer
    soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

#Recuperer  
# ● product_page_url (le lien)
    product_page_url = url
   


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
    title = soup.find(class_="product_main").h1.get_text()


   

# Ils sont tous dans un tableau d'elements : 
# ● universal_ product_code (upc)
# ● price_including_tax
# ● price_excluding_tax
# ● number_available
    UPC, price_including_tax,price_excluding_tax, number_available = "Null","Null","Null","Null"
    trs = soup.find_all("tr")
    for tr in trs:
        legend = tr.find("th").get_text() #==> en fonction de la legende 
        if legend == "UPC": # on compare
            UPC = tr.find('td').get_text()
        elif legend == "Price (incl. tax)":
            price_including_tax = tr.find("td").get_text()
            # print(tr.find("td").get_text())
        elif legend == "Price (excl. tax)":
            price_excluding_tax = tr.find("td").get_text()
        elif legend == "Availability":
            number_available = tr.find("td").get_text().replace("In stock (", "").replace(" available)","")
            
        
    # print( UPC, price_including_tax,price_excluding_tax, number_available)
        
# ● product_description
    product_description = soup.find(class_ = "sub-header").nextSibling.nextSibling.get_text()

# ● category
    liens = soup.find(class_= "breadcrumb").find_all("a")
    if len(liens) >= 3:
        category = liens[2].get_text()
    else:
        category = "Null"
    

# ● review_rating
    review = soup.find(class_= "star-rating")
    classes = review["class"]
    if len(classes) >= 2:
        rating = classes[1]
        if rating in nombres:
            review_rating = nombres[rating]
        else:
            review= "null"
    else:
        review_rating = "Null"
    
    
# ● image_url
    image = soup.find(class_ = "item active").find("img")
    image_url = image["src"]



    veille_concurrentielle.append((product_page_url,UPC, title,price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url))
    # for v in veille_concurrentielle:
    #     print(v)

# Si la page est pas ok 

 
# Resultat de la phase 1) ==>creeer un csv 
#   Que faire pour arriver a ca ? ==> 
#   Comment les stocker ? ==> Cs
#   
# Result


#csv
    with open('veille_concurrentielle.csv', 'w', newline='') as csv_concurrentielle:
        writer = csv.writer(csv_concurrentielle)
        writer.writerows(veille_concurrentielle)
        
else:
    print("Error")
    
    
    
#
