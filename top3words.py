def top_3_words(text):
    charz=" \\//,/\..?!1234567890:-_;"
    for charr in charz:
        text=text.replace(charr, " ")
    d={}
    n_t=text.split()
    for word in n_t:
        n_w=word.lower()
        if n_w=='':
            continue
        # dealing with apps --
        if "'" in n_w:
            alpha=False
            for c in n_w:
                if(c.isalpha()):
                    alpha=True
            if(alpha==False):
                continue
        # done dealing with apps --
        if n_w not in d:
            d[n_w]=1
        else:
            d[n_w]+=1
    x=sorted(d,key=d.get,reverse=True)[:3]
    return x
