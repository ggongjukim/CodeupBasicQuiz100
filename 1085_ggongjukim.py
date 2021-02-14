h,b,c,s=map(float,input().split())
bit = h*b*c*s
byte = bit / (2**3)
kb = byte / (2**10)
mb = kb / (2**10)
print('%.1f'%mb , "MB")
#비트시프트 연산은 float 안됨
