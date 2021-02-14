arr = [[0] * 19 for _ in range(19)] #2차원 초기화
for i in range(len(arr)):
    arr[i] = list(map(int, input().split()))

n = input()
for i in range(0,int(n)):
    a = list(map(int,input().split())) #10 10
    for x in range(0,len(arr)):
        arr[a[0]-1][x] = int(not arr[a[0]-1][x])
    for y in range(0,len(arr[0])):
        arr[y][a[1]-1] = int(not arr[y][a[1]-1])
        

for x in range(len(arr)): #가로행 길이
    for y in range(len(arr[0])): #세로행 길이
        print(arr[x][y],end=' ')
    print()#\n 안해도 줄바꿈됨

