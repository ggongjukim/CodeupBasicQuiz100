a = input()
i = 0
for b in a:
    print('['+str(int(b)*(10**(4-i)))+']') #"%d"를 붙여주면str로 안바꿔도 됨
    i += 1;
