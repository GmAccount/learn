# Notions à utiliser pour résoudre l'exercice :
# # dictionnaires, classes
# # ______# ENONCE# - Créer une classe Pays avec les attributs d'instance nom, population et surface
# # - Créer une méthode de calcul de la densité de population
# # - Créer une méthode d'affichage des informations de l'instance
# # - Manipuler la chaine de caractères str_pays pour créer une liste d'instances de la classePays
# # Structure de chaine de caractères : population, surface (km2), nom du pays


class Pays:
  def __init__(self,pays,population,surface):
      self.nom_du_pays=pays
      self.surface = surface
      self.population = population

  def densite(self):
      try:
        return int(self.population)/int(self.surface)
      except:
        return False

      
  def __repr__(self):
    		return "la densite de pays {} est : {:.2f}".format(self.nom_du_pays,self.densite())

#########################################

str_pays = """
36500000
447000
Maroc
201000000
924000
Nigeria
58000000
945000
Tanzanie
2500000
824000
Namibie
37400000
9971000
Canada
4200000
76000
Panama
390000
23000
Belize
44800000
2780000
Argentine
1200000
9000
Chypre
6900000
10000
Liban
5900000
488000
Turkménistan
1366400000
3287000
Inde
126900000
378000
Japon
5500000
338000
Finlande
"""


dico1=dict()

list1 = [i for i in str_pays.strip("\n").split("\n")]
for i,val in enumerate(list1):
    if i%3 == 0 :
       #print(f"pop {i} / {v}")
       #print(f" {list1[i+2]} / {list1[i+1]}")

       dico1[list1[i+2]]={"population":val,"surface":list1[i+1]}



for pays,info_dic in dico1.items():    

  #print(pays,info_dic['population'],info_dic['surface'])
  p = Pays(pays,info_dic['population'],info_dic['surface'])
  print(p)

