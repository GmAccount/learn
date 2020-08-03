

str_pays="""
36500000
Maroc
201000000
Nigeria
58000000
Tanzanie
"""

def Average(lst): 
    return sum(lst) / len(lst) 

list_population = [int(i1) for i1 in  str_pays.strip(chr(10)).split(chr(10)) if i1.isdigit() is True ]
'''
print (list_population)
'''
list_cc = [i1.upper() for i1 in  str_pays.strip(chr(10)).split(chr(10)) if (i1.isdigit() is False and i1.isalpha() is True)]
'''
print (list_cc)
'''

list_global=[]
for indice,cc in enumerate(list_cc):
    	list_global.append([cc,list_population[indice]])

list_global.sort(key= lambda x: x[1], reverse=True)

print(list_global)

moy_population= 0

try:
	moy_population = Average(list_population)
except:
	print('Verifier la liste des entiers..')


print(moy_population)











