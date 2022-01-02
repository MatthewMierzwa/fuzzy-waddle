def rgb(r, g, b):
    lst=[r,g,b]
    str_ret=""
    for i in range(0,len(lst)):
        str_app=""
        if(lst[i]<=0):
            str_ret+="00"
            continue
        elif(lst[i]>=255):
            str_ret+="FF"
            continue
        c=0
        while(lst[i]>=1):
            c+=1
            r=lst[i]%16
            lst[i]=lst[i]//16
            if(r==10):
                str_app+="A"
            elif(r==11):
                str_app+="B"
            elif(r==12):
                str_app+="C"
            elif(r==13):
                str_app+="D"
            elif(r==14):
                str_app+="E"
            elif(r==15):
                str_app+="F"
            else:
                str_app+=str(r)
        if(c==2):
            str_ret+=str_app[::-1]
        else:
            str_ret=str_ret+"0"+str_app
    return str_ret
    pass
