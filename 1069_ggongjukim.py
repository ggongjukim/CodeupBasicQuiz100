a = input()
#파이썬은 switch문을 지원하지 않는다..! -> 딕셔너리로 대체 get은 디폴트
def Switch(a):
    return{'A' : "best!!!", 'B': "good!!", 'C' : "run!", 'D':"slowly~"}.get(a,'what?')
print(Switch(a))
