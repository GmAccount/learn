from pays import Pays

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
  p = Pays(pays,**info_dic)
  #  p = Pays(pays,info_dic['population'],info_dic['surface'])

  print(p)

