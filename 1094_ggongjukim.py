n = input()
a = list(map(int,input().split()))
for i in range(len(a)):
    print(a[len(a)-1-i],end = " ")
