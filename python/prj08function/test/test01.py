def JudgeNumber(num):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"

# 임의의 정수 입력받아 홀짝 판단 하고 출력하기

#정수 입력
n=int(input("정수 : "))

#판단하기
result = JudgeNumber(n)

#출력하기
print(f"입력하신 숫자 {n}는 {result}입니다.")