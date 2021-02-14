r,g,b=map(int,input().split())
sum =0
for i in range(0,r):
    for j in range(0,g):
        for k in range(0,b):
            print(i , j , k)
            sum += 1
print(sum)
