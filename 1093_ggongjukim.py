n = input()
a = list(map(int,input().split()))
student = [0]*23
for i in a:
    student[i-1] += 1
for j in range(len(student)):
    print(student[j],end=' ')
