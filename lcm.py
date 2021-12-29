import functools

def helper(arr):
    temp=arr[0]
    temp2=arr[1]
    temp3=0
    while(temp2!=0):
        temp3=temp
        temp=temp2
        temp2=temp3%temp
    return temp

def calc_lcm(a,b):
    return (a*b)//helper([a,b])

def lcm(*args):
    if len(args)==0:
        return 1
    for i in args:
        if i==0:
            return 0
    return functools.reduce(calc_lcm, args)
