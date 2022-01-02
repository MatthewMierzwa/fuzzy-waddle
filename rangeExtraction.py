def solution(args):
    e=[]
    for q in args:
        e.append(q)
    lst=sorted(e)
    str_ret=""
    i=0
    while(i<len(lst)):
        found=False
        c=2
        str_app=str(lst[i])
        last=""
        for j in range(i+2,len(lst)):
            if(lst[i]+c==lst[j]):
                found=True
                c+=1
                last=str(lst[j])
            else:
                break
        if found:
            str_app=str_app+"-"+last
            i=i+c-1
        str_ret=str_ret+str_app+","
        i+=1
    return str_ret[0:len(str_ret)-1]
