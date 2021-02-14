n = input()
a = list(map(int,input().split()))
min = a[0]
for i in range(0,len(a)):
    if min > a[i]:
        min = a[i]
print(min)
