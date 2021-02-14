array = [[0] * 20 for _ in range(20)] #2차원 초기화
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    array[a[0]][a[1]]=1
for x in range(1,len(array)): #가로행 길이
    for y in range(1,len(array[0])): #세로행 길이
        print(array[x][y],end=' ')
    print()#\n 안해도 줄바꿈됨
