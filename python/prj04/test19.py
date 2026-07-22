# 숫자 3개를 입력받으세요.
# 첫 번째 숫자가 두 번째와 세 번째 숫자보다 모두 큰지 출력하세요.
# 숫자1: 30
# 숫자2: 20
# 숫자3: 10
# 숫자1이 가장 큰가?: True

num1=int(input("숫자1 : "))
num2=int(input("숫자2 : "))
num3=int(input("숫자3 : "))

terms=num1>num2 and num1>num3

print(f"숫자1이 가장 큰가? : {terms}")