def duplicate_count(text):
    d={}
    for ch in text:
        if ch.lower() in d:
            d[ch.lower()]+=1
        else:
            d[ch.lower()]=1
        print(d)
    c=0
    for k in d:
        if d[k] > 1:
            c+=1
    return c
