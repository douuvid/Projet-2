 #Phase 2
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



#Etape no code
    #Objectif : 
    # 1°Faire un script qui consulte la page de la categorie 
    # ==>utiliser les notions precdente een adaptant uniquement au categorie ?
    # 

    #l'URL de la page Produit de chaque livre appartenant à cette catégorie.
    #===> p;e utiliser fonction ? Si oui comment et quoi ?
    #==< utiliser .format

import requests
from bs4 import BeautifulSoup # Pour filtres les balises
import csv
from scrapers import booktoscrape  # Quand j'ai deux fichier qui va porter deux noms de focntion

from scrapers.booktoscrape import scrape_un_theme # Quand je dois utiliser une seule fonction ==>Uti cette methode<==


url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

donnees = scrape_un_theme(url)

veille_concurrentielle = [("product_page_url","universal_product_code (upc)", "title","price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url")]
if donnees != None and len(donnees) > 0:
    with open('veille_concurrentielle.csv', 'w', newline='') as csv_concurrentielle:
        writer = csv.writer(csv_concurrentielle)
        veille_concurrentielle.extend(donnees)
        writer.writerows(veille_concurrentielle)
