a = int(input())
#파이썬은 switch문을 지원하지 않는다..! -> 딕셔너리로 대체 get은 디폴트
def Season(a):
    return{ 12 : "winter",
            1 : "winter",
            2 : "winter",
            3 : "spring",
            4 : "spring",
            5 : "spring",
            6 : "summer",
            7 : "summer",
            8 : "summer",
            9 : "fall",
            10 : "fall",
            11 : "fall"
    }.get(a)
print(Season(a))
