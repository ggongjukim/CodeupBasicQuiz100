a,b = map(int,input().split()) # ~a 비트 not 
def BitAnd(i,j):
    x = bin(i & j)
    print(int(x,2))

BitAnd(a,b)
