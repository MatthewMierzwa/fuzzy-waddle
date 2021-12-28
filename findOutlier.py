def find_outlier(integers):
    o=[]
    e=[]
    for i in integers:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    if(len(o)>len(e)):
        return e[0]
    else:
        return o[0]
    return None
