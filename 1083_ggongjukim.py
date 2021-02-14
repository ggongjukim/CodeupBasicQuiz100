a =int(input())
string = ""
for i in range(1, a+1):
    if i%3 == 0:
        string = string + "X" + " "
        #print("X")
        continue
    string = string + str(i) + " "
print(string)
#이어붙여서 출력하기 print(end='')
