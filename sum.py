def sumy(x):
    
    y  = len(x)
    if y == 1:
        z = x[0]
    else:
        z = x[0]+  sum(x[1:])
    print(z)


sumy([10,20,30])
#yaha major problem tab aayegi jab ham print meh sumy(x) ki place per sumy(x{})   likengey 
#hamne yaha sumy[]   hame seedha x ki value likenki hai