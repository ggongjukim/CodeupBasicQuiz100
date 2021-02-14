w,h = map(int,input().split()) #w가로행개수 h세로행개수
arr = [[0] * h for _ in range(w)] #2차원 초기화

n = input()
for i in range(0,int(n)): #l막대길이  #d방향 #xy좌표
    l,d,x,y = map(int,input().split()) #2 0 1 1
    if(d == 0):
        for _ in range(l):
            arr[x-1][y-1]=1
            y += 1
    else:
        for _ in range(l):
            arr[x-1][y-1]=1
            x += 1
for x in range(len(arr)): #가로행 길이
    for y in range(len(arr[0])): #세로행 길이
        print(arr[x][y],end=' ')
    print()#\n 안해도 줄바꿈됨
