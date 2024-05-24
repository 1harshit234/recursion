def recursiv(y):
   
    total = 0
    
    
    for x in y:
        
        if type(x) == type([]):

            total = total + recursiv(x)
        else:
        
            total = total + x

   
    return total


print(recursiv([1, 2, [3, 4], [5, 6]]))