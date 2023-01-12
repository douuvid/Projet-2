import requests
from bs4 import BeautifulSoup  # Pour filtres les balises

nombres = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

def scrape_un_livre (url):
   
    r = requests.get(url)

    if r.ok:
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')
        
        product_page_url = url
    
        title = soup.find(class_="product_main").h1.get_text()

        UPC, price_including_tax,price_excluding_tax, number_available = "Pas à trouver","Pas à trouver","Pas à trouver","Pas à trouver"
        trs = soup.find_all("tr")
        for tr in trs:
            legend = tr.find("th").get_text()
            if legend == "UPC": # on compare
                UPC = tr.find('td').get_text()
            elif legend == "Price (incl. tax)":
                price_including_tax = tr.find("td").get_text()
            elif legend == "Price (excl. tax)":
                price_excluding_tax = tr.find("td").get_text()
            elif legend == "Availability":
                number_available = tr.find("td").get_text().replace("In stock (", "").replace(" available)","")

        product_description = soup.find(class_ = "sub-header").nextSibling.nextSibling.get_text()

        #lien abolut ou relatif
        liens = soup.find(class_= "breadcrumb").find_all("a")
        if len(liens) >= 3:
            category = liens[2].get_text()
        else:
            category = "Null"

        review = soup.find(class_= "star-rating")
        classes = review["class"]
        if len(classes) >= 2:
            rating = classes[1]
            if rating in nombres:
                review_rating = nombres[rating]
            else:
                review= "Pas à trouver"
        else:
            review_rating = "Pas à trouver"
        
        image = soup.find(class_ = "item active").find("img")
        image_url = image["src"]

        return (product_page_url,UPC, title,price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url)
        
    else:
        #print("Erreur pendant le scraping du livre " + url + " : erreur HTTP "+ str(r.status_code))
        raise Exception("Erreur pendant le scraping du livre " + url + " : erreur HTTP "+ str(r.status_code))# ==> interrompre l'execu 
        


# Modif : Scrape les livres d'une pages qui scrape les livr
        
def scrape_des_livres(urls):
    info_livres =[]

#STOCKER LES INFO DES LIVRE DAN SUN TABLEAU ET PRINT TABLEAU 
    for url in urls:
        donnees = scrape_un_livre(url)
        if donnees != None:
            info_livres.append(donnees)
    return info_livres






def scrape_un_theme(url):
    # stocker les donner dans un tableau 
    info_livres= []
    
    
    next = url
    while next != None:
                #je fai sqqch 
                # Si c'zt plus egale a none je faisautre chose 
                
                resultat = recupere_page(next)
                next = resultat[1]
                info_livres.extend(resultat[0])
                
    # date 2/01  :  Exo a faire pour le 9/01 
    # return scrape_un_theme_while(url) creer une autre un eboucle while (une conditoon pour boucle , tant que le bouton next )
    #calculer une condition 
                #1° Creation de la boucle while 
                    # Y integrer la condtion tant que le bouton next existe donc tant que c'est true scrap
                    #1) tant que next
    return info_livres
                    
                    
                    
                    
                    
                    
                    
                    
    
    
def scrape_un_theme_recur(url): 
    if len(url) == 0:
        return
    
    r = requests.get(url)

    if r.ok:
    # vérifier que la page est bien

    #Je creer un tableau qui recup les url 
        urls_livres = []
    #parcer
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        liens_image = soup.find_all(class_="image_container")
        
        for i in liens_image: # Pour chaque elemement  ==> Ici, l'objectif est de recupere les liens 
            a = i.find("a") # stocker le resultzt attendu 
            urls_livres.append(a["href"].replace("../../../","http://books.toscrape.com/catalogue/"))# Le resultat attendu tu le renvoie dans ta 
            #LES ATTRIVBUE SE LISENT COMME DES LISTES 
        resultat = scrape_des_livres(urls_livres)

        next = soup.find(class_= "next") # Cette partie traite de next 
        if next != None:
            lien = next.find("a")["href"]
            
            
            #  date 2/01  :  Exo a faire pour le 9/01 
            # Changer utiliser les methode dans str() pour aider  https://docs.python.org/fr/3/library/stdtypes.html#text-sequence-type-str
            # 1° tout lire a partir Méthodes de chaînes de caractères sauf le case/center(ne pas lire ) ; lire la cont+ endw + find + format + index + lire is mais ne pas s'y att + join+ strip+ replace + rfind  ==> Tout ca sera uti dans le parcours +split +strip
            #2 ===> Permet d'eco des lignes + permet de supprimer la boucle fort 
            #3° Faire des exo perso 
            #4 essayer de trouvr 3 maniere de rempl la boucle for  avec les methode
            #   Une maniere qui utili find ou rfind ( commence par la droite) 
            
            
            
            #Split et join
            
            
        
            while next != None:
                #je fai sqqch 
                # Si c'zt plus egale a none je faisautre chose 
                
                next = recupere_page(url)[1]
                print(next)
            
            
            
                
            
            # utiliser 
            #join(iterable) :
            # Renvoie une chaîne qui est la concaténation des chaînes contenues dans iterable. Une TypeError sera levée si une valeur d'iterable n'est pas une chaîne, y compris pour les objets bytes. Le séparateur entre les éléments est la chaîne fournissant cette méthode.

            
            
            # Avantage / inconveniant 
            # des fonction recur
                # Rapp une methode augmente la stack, utilise plus de memoire 
                # recherche les avantage inco 
                # Savoir faire les deux pour pouvoir fair el emeilleur choix car impacte dur la memoire
            
        
            #for index in range(len(url)-1, -1, -1): # star, stop, step => len affiche la laongueur du tableau et range reitere
               # if url [index] == '/':
                 #   lien_remplace = url[0:index+1] + lien 
                  #  donnees = scrape_un_theme(lien_remplace)
                   # if donnees != None and len(donnees) > 0 :
                   #     resultat.extend(donnees)
                   # break
                   
        return(resultat)
    else:
        print("Erreur pendant le scraping de la page " + url + " : erreur HTTP "+ str(r.status_code))
        
        

def recupere_page (url):
    lien_recolle = None
    
    if len(url) == 0:
        raise Exception("Erreur pendant le scraping du livre : url est vide ") #Quand y a une erreur 
    
    r = requests.get(url)

    if r.ok:
    # vérifier que la page est bien

    #Je creer un tableau qui recup les url 
        urls_livres = []
    #parcer
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')

        liens_image = soup.find_all(class_="image_container")
        
        for i in liens_image: # Pour chaque elemement  ==> Ici, l'objectif est de recupere les liens 
            a = i.find("a") # stocker le resultzt attendu 
            urls_livres.append(a["href"].replace("../../../","http://books.toscrape.com/catalogue/"))# Le resultat attendu tu le renvoie dans ta 
            #LES ATTRIVBUE SE LISENT COMME DES dico
        resultat = scrape_des_livres(urls_livres)
        next = soup.find(class_= "next") # Cette partie traite de next 
        if next != None:
            lien = next.find("a")["href"]
            lien_coupe_par_la_droite = url.rsplit("/",maxsplit=1)
                # tant que le bouton next exite concatene 
            lien_coupe_par_la_droite[1] = lien
            lien_recolle = "/".join(lien_coupe_par_la_droite)
            
        
  
            
        return resultat, lien_recolle
    
    
    
    else:
        #print("Erreur pendant le scraping du livre " + url + " : erreur HTTP "+ str(r.status_code))
        raise Exception("Erreur pendant le scraping du livre " + url + " : erreur HTTP "+ str(r.status_code))# ==> interrompre l'execu 
    

    
    




def scrap_un_site(url):
    info_site = []
    r = requests.get(url)
    
    if r.ok:
        #utiliser soup pour trouver des element 
        soup = BeautifulSoup(r.content.decode('utf-8','ignore'), 'html.parser')
        liens = soup.find(class_ = "nav nav-list")
        for lien in liens:
            
            a = lien.find("a")
            #transformer un lien relatif en absolut
            lien_relatif = a["href"]
            trans_lien_relatif_en_absolut
            
            
            
            
            
            resultat =scrape_un_theme(url)
        return resultat
            
            # mettre touts les liens dans un cv
            
            
            
        
   
        
    else:
        raise Exception("Erreur pendant le scraping du site "+ url)
        
    
#fair eun fichier par donc for categorie 
#pour chaquz lien lien un csv 


def trans_lien_relatif_en_absolut (url, lien_relatif):
    
    url_split = url.split("/")
    # Renvo
    url_split = url_split[:-1]
    # cherche le possiblite
    for split in url_split:
        if split == ".":
            continue
        elif split == "..":
            url_split = url_split[:-1]
        else:
            url_split.append(split)
        

    lien_absolut = "/".join(url_split)
    
    return lien_absolut 
