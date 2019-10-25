def convert(n):
    r=""
    if n%3==0:
        r+="Pling"
    if n%5==0:
        r+="Plang"
    if n%7==0:
        r+="Plong"
    if(n%3!=0 and n%5!=0 and n%7!=0):
        r+=str(n)
    return r
