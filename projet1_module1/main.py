"""
#---------# PROJET -#---------
# PARTIE 1 : DEMARRAGE DU PROJET ET CREATION DE LA BASE DE DONNEES
#  - Créer les différents modules du projet 
#  - Créer l'environnement virtuel avec la ou les librairies nécessaires
#  - Créer une base de données SQLite
#  - Créer une table Pays pour stocker le nom du pays et son code
#  - Récupérer les informations du fichier code_pays.csv (249 pays)
#  - Insérer les données dans la base de données 

PARTIE 2 : RECUPERATION DE DONNEES D'UNE API

# - Etudier le fonctionnement de l'API https://date.nager.at/Api
# - Pour chaque pays de fichier texte, créer une fichier JSON avec les jours fériés de# l'année 2017 grâce à un appel à l'API

PARTIE 3 : STOCKAGE DE LA DONNEE EN BASE DE DONNEES

# - Créer une nouvelle table dans la base de données pour stocker les jours fériés
# - Insérer les données des fichiers JSON dans la nouvelle table

PARTIE 4 : ANALYSE DES DONNEES DE LA BASE

#  - Afficher le pays qui a le plus de jours fériés en 2017 à partir d’une requête SQL sur la base de données

#  - Afficher le pays qui a le moins de jours fériés en 2017 à partir d’une requête SQL sur la base de données
#  - Afficher la liste des jours de l’année 2017 qui ne sont fériés dans aucun pays du monde à partir d’une requête SQL sur la base de données
"""


from csv import reader
from bdd import CountriesHolidays
from api import API





db_obj = CountriesHolidays()

db_obj.drop_table("countries_codes")
db_obj.drop_table("countries_holidays")

db_obj.create_table_countries()
db_obj.create_table_holidays()


with open('pays.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)

    countries_dict={}

    for row in csv_reader:
        cc = row[2] 
        country = row[4]

        country = country.replace("'","\\'");



        db_obj.insert_db("countries_codes",{ "nom_pays" : country, "country_code" : cc })


        
        
        pays = API(cc)
        res_api = pays.get_holidays()
        if res_api is not False:
          for dic2 in res_api:
                dic2['fixed'] = '1' if dic2['fixed'] else '0'
                dic2['global'] = '1' if dic2['global'] else '0'
                dic2['counties'] = str(dic2['counties'])
                dic2['type'] = str(dic2['type'])
                dic2['launchYear'] = str(dic2['launchYear'])


                dic2['localName']=dic2['localName'].replace("'","\\'");
                dic2['name']=dic2['name'].replace("'","\\'");



                #print(dic2)
                db_obj.insert_db("countries_holidays", dic2 )
                continue
                
                #  {'date': '2017-12-24', 'localName': 'Christmas Eve', 'name': 'Christmas Eve', 'countryCode': 'GL', 'fixed': True, 'global': True, 'counties': None, 'launchYear': None, 'type': 'Public'}
                
                
res_max = db_obj.get_country_min_max_holiday(min_or_max="max")                 

if res_max is not False:
      print("The country having more holidays days is : {} with {} days".format(res_max[0],res_max[1]))

res_min = db_obj.get_country_min_max_holiday(min_or_max="min")                   

if res_min is not False:
      print(res_min)
      print("The country having less holidays days is : {} with {} days".format(res_min[0],res_min[1]))
        
        #print (res_api.load_countries())

list_alldays_2017 = pays.get_alldays2017()


all_holidays_days = db_obj.select_all_dates()

for d1 in list_alldays_2017:
      if d1 not in all_holidays_days:
            print (d1)




