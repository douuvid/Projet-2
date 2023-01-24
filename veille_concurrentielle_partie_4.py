# Phase 4
# Enfin, prolongez votre travail existant pour télécharger et enregistrer le fichier
# image de chaque page Produit que vous consultez.


# En resumer ==> creer un dossier pour extraire les images 
# peur etre utiliser scrape site + BS +a href + 

#il va lme manquer un parametrre par fonction 
# cherche la maniere comment exrtraire une image 
#rajouter un parametre a la f scrap un livre

# os. path join 
#creattion de repertoire os.makedirs(path)


# Creation du repertoire 

import logging # permet de faire des log
import os
import requests
from bs4 import BeautifulSoup # Pour filtres les balises
import csv
import sys

from scrapers.booktoscrape import scrap_un_site, recup_image
output_path = sys.argv[1]


logging.basicConfig(level=logging.INFO)#configure le module logging
url = "https://books.toscrape.com/index.html" # Site tout court
image_directory = "images_projet_2"
csv_directory = " results" 
parent_dir = '/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet-2' # chemin  absolu (qui part de la racine de votre système de fichier )

image_path = os.path.join(output_path, image_directory)
os.makedirs(image_path,exist_ok = True)
os.makedirs(os.path.join(output_path,csv_directory) ,exist_ok = True)

logging.info(f"Scraping site {url}")
donnees = scrap_un_site(url)
liste_livres= donnees["Books"]

for livre in liste_livres:
    recup_image(livre [-1],image_path)

    

for type in donnees:
    donnees_livres = donnees[type]
    veille_concurrentielle = [("product_page_url","universal_product_code (upc)", "title","price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url")]
    if len(donnees_livres) > 0:
        with open(os.path.join(output_path,csv_directory,'veille_concurrentielle_'+ type +'.csv'), 'w', newline='') as csv_concurrentielle:
            writer = csv.writer(csv_concurrentielle) # --> class class csv.DictWriter utilise un dictionnaire https://docs.python.org/3/library/csv.html
            veille_concurrentielle.extend(donnees[type])
            writer.writerows(veille_concurrentielle)
        
        
        

# se renseigner sur logging