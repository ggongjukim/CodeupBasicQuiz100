a = int(input())
i = 1
sum = 1
for i in range(i,a):
    sum += i
    if sum <= a:
        i+=1
    elif sum > a:
        break
print(i)
