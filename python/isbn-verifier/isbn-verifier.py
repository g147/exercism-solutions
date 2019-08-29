import re
def is_valid(isbn):
    isbn=re.findall(r'[0-9X]',isbn)
    a=10; r=0
    if len(isbn)!=10:
        return False
    for i in isbn:
        if i=='X':
            r+=10
        else:
            r+=a*int(i)
        a-=1
    return r%11==0
