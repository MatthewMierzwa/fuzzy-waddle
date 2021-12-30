def find_it(seq):
    d={}
    for i in seq:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k in d:
        if d[k]%2!=0:
            return k
    return None
