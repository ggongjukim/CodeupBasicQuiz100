a,b = map(int,input().split()) 
def SameTrue(i,j):
    if(i == j):
        return 1
    else:
        return 0
print(SameTrue(bool(a),bool(b)))
