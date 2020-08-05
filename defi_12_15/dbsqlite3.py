import sqlite3


class Countries:
  def __init__(self,file_name="data.db"):
    self.conn=sqlite3.connect(file_name)
    self.cursor=self.conn.cursor()

  def create_table(self):
        """ Make new table  """
        try:
          self.cursor.execute('''create table if not exists countries (nom_pays TEXT,capitale TEXT,
          population_1 INTEGER,surface INTEGER)''')
          self.conn.commit()

        except Exception as e: 
          print("Problem to create the table")
          print(e)
        else:
          print("Table Created")

  def drop_table(self):
        """ drop table  """
        try:
          self.cursor.execute('''drop table if exists countries''')
          self.conn.commit()

        except Exception as e: 
          print("Problem to drop the table")
          print(e)
        else:
          print("Table removed")

  def insert_db(self,nom_pays,capitale,population_1,surface):
        """ insert countries info """

        try:
          self.cursor.execute("INSERT INTO countries(nom_pays,capitale,population_1,surface) VALUES (?,?,?,?)",(nom_pays,capitale,population_1,surface))
          self.conn.commit()
        except Exception as e:
          print(f"Problem to insert data {nom_pays},{capitale},{surface},{population_1} in the database")
          print(e)
        else:
          print("Record inserted") 

  def select_data(self):
      """ Select data from database"""
      try:
        self.cursor.execute("SELECT nom_pays,population_1 FROM countries ORDER BY population_1 DESC LIMIT 5")
        result=self.cursor.fetchall()
        print("Liste des 5 pays les plus peuplés:")
        j=1
        for elt in result: 
           print(f"{j}  /  {elt[0]}:{elt[1]}")
           j+=1
      except Exception as e:
        print("Problem with the select query")
        print(e)   



if __name__== "__main__":
    cc = Countries()
    print(cc)
    cc.drop_table()
    cc.create_table()
    cc.insert_db("ma","Rabat",33000000,447000)
    cc.insert_db("ng","ng_capitale",201000000,924000)
    cc.select_data()




    
