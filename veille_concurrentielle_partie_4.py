# Phase 4
# Enfin, prolongez votre travail existant pour télécharger et enregistrer le fichier
# image de chaque page Produit que vous consultez.


import requests
from bs4 import BeautifulSoup  # Pour filtres les balises
from scrapers import booktoscrape

url ="http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

booktoscrape.scrape_un_theme(url)

