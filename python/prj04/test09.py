# 사용자의 나이를 입력받으세요.
# 다음 중 하나라도 만족하면 `True`가 나오도록 작성하세요.
# - 13세 이하
# - 65세 이상
# 나이: 70
# 할인 대상: True

User_age=int(input("나이 : "))
under13= User_age <= 13
over65= User_age >= 65
terms=under13 or over65

print(f"할인 대상 : {terms}")