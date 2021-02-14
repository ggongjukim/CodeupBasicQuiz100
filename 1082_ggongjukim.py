a = int(input(),16) #16진수를 10진수로 만듦
b = int('F',16) 
for i in range(1, b+1):
    c = a * i
    print('%X'%a + "*"+ '%X'%i +"="+'%X'%c) #%X 10진수를 16진수 형태로 출력
