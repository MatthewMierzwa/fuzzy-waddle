import math
def number_of_pairs(gloves):
    d={}
    for i in gloves:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    c=0
    for k in d:
        c+=math.floor(d[k]/2)
    return c
