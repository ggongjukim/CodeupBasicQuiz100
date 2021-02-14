a,m,d,n = map(int,input().split())
for _ in range(1,n):
    a = a * m + d
print(a)
