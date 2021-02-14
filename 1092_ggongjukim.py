a,b,c = map(int,input().split())
i =1
while True:
    if(i%a == i%b == i%c == 0):
        print(i)
        break
    i += 1
