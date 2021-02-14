a = map(int, input().split()) #list를 하고 안하고 무슨찬이? type은 map이 무슨의미?
for x in a:
    if x != 0:
        print(x)
    else:
        break
