>>> 
>>> list_comp=["pair" if i%2==0 else "impair" for i in range(10)]              
>>> print (list_comp)                                            
['pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair']
>>> list_comp=["pair" if i%2==0  for i in range(10)]             
  File "<stdin>", line 1
    list_comp=["pair" if i%2==0  for i in range(10)]
                                   ^
SyntaxError: invalid syntax
>>> list_comp=["pair" if i%2==0 else "impair" for i in range(10)]
>>> 
>>> 
>>> print (list_comp)                                            
['pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair']
>>> 
>>> 
>>> dict_comp={i:("pair" if i%2==0 else "impair") for i in range(9)} 
>>> 
>>> 
>>> 
>>> dict_comp
{0: 'pair', 1: 'impair', 2: 'pair', 3: 'impair', 4: 'pair', 5: 'impair', 6: 'pair', 7: 'impair', 8: 'pair'}
>>> 
>>> 
>>> 
>>> dict_comp={i:("pair" if i%2==0 else "impair") for i in range(9)}
>>> 
>>> dict_comp={i:"pair" if i%2==0 else "impair" for i in range(9)}  
>>> dict_comp
{0: 'pair', 1: 'impair', 2: 'pair', 3: 'impair', 4: 'pair', 5: 'impair', 6: 'pair', 7: 'impair', 8: 'pair'}
>>> dict_comp1={i:"pair" if i%2==0 else "impair" for i in range(9)}
>>> dict_comp1
{0: 'pair', 1: 'impair', 2: 'pair', 3: 'impair', 4: 'pair', 5: 'impair', 6: 'pair', 7: 'impair', 8: 'pair'}
>>> dict_comp1={i:"pair" if i%2==0 else "impair" for i in range(9)}
>>> 
>>> 