"""
Voici les différentes étapes du défi :
● Créer un environnement virtuel pour le défi
● Installer la librairie requests dans cet environnement virtuel
● Créer une requête à l'API https://restcountries.eu/rest/v2/all pour récupérer un JSON des données des pays (si l’url ne fonctionne plus, utiliser directement le fichier JSON)
● Afficher le résultat de la requête et créer un fichier JSON du résultat
● Créer une base de données SQlite avec une seule table Pays pour stocker le nom, la capitale, la population et la surface
● Insérer les données dans la base SQLite
● Créer une requête sur la base de données pour récupérer les 5 pays les plus peuplés

"""

import json, requests, sys
from dbsqlite3 import Countries
 
try:
  res = requests.get("https://restcountries.eu/rest/v2/all")
except Exception as e:
  print("Error while getting json online..."+str(e))
  sys.exit()
else:
  print(res)

list1 = res.json()

with open("/tmp/temp_cc.json","w") as file2write:
  file2write.write(json.dumps(list1))



dico_pays = {}

cc = Countries()
cc.drop_table()
cc.create_table()

for i1 in list1:
      dico_pays["nom_pays"] = i1["name"]
      dico_pays["capitale"] = i1["capital"]
      dico_pays["surface"] = i1["area"]
      dico_pays["population_1"] = i1["population"]


      #cc.insert_db("ma","Rabat",33000000,447000)
      cc.insert_db(**dico_pays)
    
      #print("=---------=")

cc.select_data()


