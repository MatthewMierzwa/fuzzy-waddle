def order(sentence):
    l=sentence.split()
    n=[]
    for i in l:
        for c in i:
            if c.isnumeric():
                n.append((c,i))
    for i in range(0,len(n)):
        min=n[i][0]
        index=i
        for q in range(i+1,len(n)):
            if n[q][0]<min:
                min=n[q][0]
                index=q
        temp=n[i]
        n[i]=n[index]
        n[index]=temp
    ret=""
    for qq in n:
        ret=ret+qq[1]+" "
    return ret.rstrip()
