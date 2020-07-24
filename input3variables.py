import sys
somme=0
i=1
minVal,maxVal=(None,None)
list_3_values=list()


while i<=3:
    print ("iteration {} ...".format(i))
    input_var = input("Enter an integer : ") 

    try:
        input_var = int(input_var)
    except:
        print ("this input {} is not integer...".format(input_var))
        continue

    list_3_values.append(input_var)  
    i=i+1


for j in list_3_values:
    """
    trying to have min value
    """
    if minVal is None: 
        minVal=j
    elif j<minVal:
        minVal=j



    """
    trying to have max value
    """
    if maxVal is None: 
        maxVal=j
    elif j>maxVal:
        maxVal=j

    




    
    
    somme=somme+int(j)

print ("The sum is :  {}".format(somme))  
print ("The max value is :  {}".format(maxVal))  
print ("The min value is :  {}".format(minVal))    
