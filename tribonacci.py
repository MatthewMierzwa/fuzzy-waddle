def tribonacci(signature, n):
    if(n==0):
        return []
    q=len(signature)
    if(n<q):
        return signature[0:n]
    off=n-q
    c=0
    added=0
    for i in range(0,off):
        signature.append(sum(signature[added:]))
        added+=1
    return signature
