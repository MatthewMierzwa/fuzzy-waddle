def Xbonacci(signature,n):
    q=len(signature)
    if(n<=q):
        ret=[]
        for e in range(0,n):
            ret.append(signature[e])
        return ret
    off=n-q
    added=0
    c=0
    while(added<off):
        for i in range(added,q+added):
            c+=signature[i]
        signature.append(c)
        added+=1
        c=0
    return signature
