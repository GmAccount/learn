import sys
somme=0

i=1
minVal,maxVal=(None,None)

while i<=3:
    print ("iteration {} ...".format(i))
    input_var = input("Enter an integer : ") 

    try:
        input_var = int(input_var)
    except:
        print ("this input {} is not integer...".format(input_var))
        continue

    """
    trying to have min value
    """
    if minVal is None: 
        minVal=input_var
    elif input_var<minVal:
        minVal=input_var



    """
    trying to have max value
    """
    if maxVal is None: 
        maxVal=input_var
    elif input_var>maxVal:
        maxVal=input_var

    




    i=i+1
    
    print (input_var)
    somme=somme+int(input_var)

print ("The sum is :  {}".format(somme))  
print ("The max value is :  {}".format(maxVal))  
print ("The min value is :  {}".format(minVal))    
