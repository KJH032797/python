print("program start")

try:
    x = int(input("x:"))
    y = int(input("y:"))
except Exception as e:
    print("0을 제외한 숫자만 입력해주세요")
    print(type(e))
    print(e)
else :
    result = x / y
    print(result)
    print("정상 실행 되었습니다")
finally:
    print("마지막에 무조건 실행")

print("program finish")