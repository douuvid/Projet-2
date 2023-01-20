import numpy as np


# def replace(str,remplacer,remplacant):
#     #prendre des string entre , les recherhce et les remplacer par une autre string 
    
#     i = 0
    
#     while i < len(str):
#         for 
        
        
        
#         i += 1 
        
     
            
        
#     return str

# def replace (str, remplacer, remplacant):
#     length_diff = len(str)- len(remplacer)
#     if length_diff >= 0 :
#         length_diff_remplace = len(remplacer)- len(remplacant)
#         i = 0
#         while i <= length_diff:
#             if str[i:i+len(remplacer)] == remplacer:
#                 str = str[:i] + remplacant + str[i+len(remplacer):]
#                 length_diff -= length_diff_remplace
#             i += 1
#     return str







# print(replace("test", "t", "u"))
# print(replace("test", "tes", "u"))
# print(replace("test", "t", "ou"))
# print(replace("ttttttttt", "tt", "u"))
# print(replace("tttttttttt", "tt", "u"))


#faire deux fonction
    # find in  list et find in  dictionnaire 
    #leur donner une clef a trouver de dans 
    # 
    
# liste = [{"cle": "test", "valeur": {"data": "caca"}}, {"cle": "test2", "valeur": {"data": "caca"}}, {"cle": "youpi", "valeur": "trouvé"}]
# dictionnaire = {"test": {"data": "caca"}, "test2": {"data": "caca"}, "youpi": "trouvé"}


# def find_in_list(list, key):
    
#     #Parcourir le disco , dire au momement ou tu trouve sa faire sa
    
#     for element in list:
#         if element ["cle"] == key:
#             return element["valeur"]
        
        
# def find_in_doci(dico,key):
#     return dico[key]
        
        
# print(find_in_list(liste, "test2"))
# print(find_in_doci(dictionnaire, "youpi"))

#faire un logiciel pour la gestion d'un park auto 
#un park de 20place , 2 ranger de 10
#les voiture ne peuvent pas se garer au meme endroit
# Quan dune voiture est vendu  elle est sorti du parking ; son prix est ajouter au compte en banque 


place_de_parking=[(1,2,3,4,5,6,7,8,9,10)* 2]
total_place = 20 
banque = 20000


class Voiture:
    posseder = False
    
    def prix_de_vente (self):
        return self.achat*1.30
    
    def __init__(self, plaque,achat,marque,moteur="cs5"):
        
        
        self.plaque = plaque
        self.achat= achat
        self.moteur=moteur
        self.marque= marque 
        
        
    def acheter(self, banque):
        
        if banque < self.achat:
            raise Exception("Vous manquez de fonds")
        if self.posseder:
            raise Exception("Achat deja effectué")
        self.posseder = True
        return banque - self.achat
    
    def vendre(self, banque):
        if not self.posseder:
            raise Exception("Vous ne disposez pas cette voiture dans le parking")
        self.posseder = True
        return  banque + self.prix_de_vente()
        

        
        

    
renault = Voiture("azert", 4000, "zoe")
print(banque)

banque = renault.acheter(banque)
banque = renault.vendre(banque)
print(banque)


