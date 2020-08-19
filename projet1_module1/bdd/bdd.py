import sqlite3
import logging


class CountriesHolidays:
  def __init__(self,file_name="data.db"):
    self.conn=sqlite3.connect(file_name)
    self.cursor=self.conn.cursor()

  def create_table_holidays(self):
        """ Make new table  """
        #   {'date': '2017-12-24', 'localName': 'Christmas Eve', 'name': 'Christmas Eve', 'countryCode': 'GL', 'fixed': True, 'global': True, 'counties': None, 'launchYear': None, 'type': 'Public'}

        try:
          self.cursor.execute('''create table if not exists countries_holidays (
          date TEXT,
          localName TEXT,
          name TEXT,
          countryCode TEXT,
          fixed TEXT,
          global TEXT,
          counties TEXT,
          launchYear TEXT,
          type TEXT
          )''')
          self.conn.commit()


        except Exception as e: 
          logging.critical("Cannot make table holidays...{}".format(e))
        else:
          logging.debug("Table holidays created")


  def create_table_countries(self):
        """ Make new table  """
        try:
          self.cursor.execute('''create table if not exists countries_codes (nom_pays TEXT,country_code TEXT)''')
          self.conn.commit()

        except Exception as e: 
          logging.critical("Cannot make table countries_codes...{}".format(e))
        else:
          logging.debug("Table countries_codes created")

  def drop_table(self,table_name):
        """ drop table  """
        try:
          self.cursor.execute('''drop table if exists {}'''.format(table_name))
          self.conn.commit()

        except Exception as e: 
          logging.critical("Problem to drop the table {}".format(e))
        else:
          logging.debug("Table Removed")


  def insert_db(self,table_name,dict2insert):
        """ insert  info """



        try:
          
          #self.cursor.execute("INSERT INTO {}({}) VALUES (?,?)".format(table_name,",".join(dict2insert.keys())),(tuple(dict2insert.values())))
          req = 'INSERT INTO {}({}) VALUES ("{}")'.format(table_name,",".join(dict2insert.keys()),'","'.join(dict2insert.values()))
          # self.cursor.execute("INSERT INTO {}({}) VALUES ('{}')".format(table_name,",".join(dict2insert.keys()),"','".join(dict2insert.values())))
          self.cursor.execute(req)

          self.conn.commit()
        except Exception as e:
          logging.critical("Problem to insert data into the database....{} , {}".format(req,e))
        else:
          logging.debug("Record inserted") 



  def get_country_min_max_holiday(self,min_or_max="max"):
      """ Select data from database"""

      orderBy = "desc" if min_or_max == "max" else "asc"

      req = "select countryCode,count(*) as nb from countries_holidays  group by countryCode order by nb "+orderBy+" limit 1"

      try:
        self.cursor.execute(req)
        record = self.cursor.fetchone()
        return record
           
      except Exception as e:
        logging.warning("Problem with the select query..{}".format(e))

      return False

  def select_all_dates(self):
      """ Select data from database"""


      list_temp = []

      try:
        self.cursor.execute("SELECT distinct date FROM countries_holidays")
        result=self.cursor.fetchall()
        for elt in result: 
           #print(f"  {elt[0]}    ")
           list_temp.append(elt[0])

      except Exception as e:
        logging.warning("Problem with the select query..{}".format(e))
        
        
      return list_temp


if __name__== "__main__":
    cc = CountriesHolidays()
    """
    print(cc)
    cc.drop_table()
    cc.create_table()
    cc.insert_db("ma","Rabat",33000000,447000)
    cc.insert_db("ng","ng_capitale",201000000,924000)
    cc.select_data()
    """
    print (len(cc.select_all_dates()))



    
