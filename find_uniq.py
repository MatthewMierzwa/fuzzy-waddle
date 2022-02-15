def find_uniq(arr):
    d={}
    for i in range(0,len(arr)):
        if arr[i] not in d:
            if len(d)==0:
                d[arr[i]]=1
                continue
            # anything past this point we've officially seen both numbers!
            elif len(d)==1:
                if d[arr[i-1]] > 1:
                    return arr[i] # we've found unique !
            d[arr[i]]=1 # not rly neccessary :/
            if arr[i]==arr[i+1]: # next is same
                return arr[i-1]
            else:
                return arr[i]
        else:
            d[arr[i]]+=1
    # your code here
    return n   # n: unique number in the array -- never gonna reach this lol
