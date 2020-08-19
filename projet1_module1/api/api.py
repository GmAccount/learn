import json, requests, sys
import logging
from datetime import date, timedelta

 

class API:
      def __init__(self,cc):
            self.cc = cc
             
      def get_holidays(self):

        list1 = []  

        url = "https://date.nager.at/api/v2/PublicHolidays/2017/{}".format(self.cc)



        try:  
          res = requests.get(url)
        except Exception as e:          
          logging.critical("Error while getting json online..."+str(e))


        if res.status_code != 200:
            logging.warning("Cannot get result from : {} ".format(url))
            return False
   
        var1 = res.json()
        """
        if isinstance(var1,dict):
              print('==dic==>')
              print(var1)
              for key1,val1 in var1.items():
                    print('==dic==>')
                    #list1.append()
        """
        if isinstance(var1,list):
                    #print('==list==>')
                    #print(var1)
                    #list1.append()
                    return var1           

        return False
       
      def get_alldays2017(self):
        sdate = date(2017, 1, 1)   # start date
        edate = date(2017, 12, 31)   # end date

        delta = edate - sdate       # as timedelta
        list2017 = []
        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            date1 = day.strftime("%Y-%m-%d")
            list2017.append(date1)
            #print(date1)

        return list2017

if __name__ == '__main__':
    pays = API("MA")
    res = pays.get_holidays()
    if res is not False:
          for i in res:
                print (i)

    print(len(pays.get_alldays2017()))