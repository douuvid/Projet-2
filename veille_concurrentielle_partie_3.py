# Phase 3
# Ensuite, étendez votre travail à l'écriture d'un script qui consulte le site de Books
# to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les
# informations produit de tous les livres appartenant à toutes les différentes
# catégories. Vous devrez écrire les données dans un fichier CSV distinct pour
# chaque catégorie de livres.


# No code 

#Bilan
    # On sait scrap un livre
    # On sait scrapt des livre dans des categorie 
    # On sait scrap des livre dans des theme different dans des pages differente 
    
# ====> L'objectif est de scrap tout le site d'un coup en mode boum ta le site tu sais ce qui y a de dans <====

# Consulter 
    # recuperer l'url 
    # voir si la requete est valider ou pas 
    
    
# Extraire les donnees des categories
    # On entend quoi par extraire ? 
        # Parcourir les categorie 
            # Parcourir les livre et rep les info
        # ==> Recuper les donnée qu'on a besoin  et stocker 
        # utiliser la fonctione extraire donner par theme 
        
    
    # Puis en fonction de la categorie 
        # extraire les donne 
            # tableau vielle concu ==> hearder : theme , nom etc 
            
# ==> Extraire toutes les categorie dans un csv a part 
    # Chaque categorie doit avoir son csv
    

# Conseille def  utiliser des long a ralonge en anglais 
    # 5 - 10 etapes  par fonction
        # chaque fonction doit etre claire et precis sans raj de comm '
    #
    
    
# fonction parcourir toutes:  recupere + parcourir les nom des cate + aller a dans la page de la categorie +
# Apres ectraction 

# Si je devais decrire etape par etape chaque a l'ordi , lui expliquer etape par etape tous ce qui doit faire pour obtenir ce que je vx + Precsion au max 
    
    
# 1)Reflecir aux fonctions que j'aurais besoin 
#2) En sous morceau jusqu'a savoir comment coder 
#3)pour arrive a l'obtif 



import requests
from bs4 import BeautifulSoup # Pour filtres les balises
import csv
from scrapers import booktoscrape


# Verifier si  ou je me trouve


    
    
# voir si la requete est valider ou pas 