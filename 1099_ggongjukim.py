m=[] #배열 입력받기 
for i in range(10): #가로행개수
    m.append([])
    a=input().split()
    for j in range(10):#세로행개수
        m[i].append(int(a[j]))
i = 2-1
j = 2-1
#m[i][j]=9
while(True):
    if m[i][j]==2:
        m[i][j]=9
        break
    elif i == 8 and j == 8:
        m[i][j]=9
        break
    elif m[i+1][j]==1 and m[i][j+1]==1:
        m[i][j]=9
        break
    
    m[i][j]=9
    #print(i,j,m[i][j])
    
    if m[i][j+1]==1:
        i+=1
    else:
        j+=1

#배열 출력하기
for x in range(len(m)): #가로행 길이
    for y in range(len(m[0])): #세로행 길이
        print(m[x][y],end=' ')
    print()#\n 안해도 줄바꿈됨
