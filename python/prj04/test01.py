# 현재 연도를 2026이라 할 때 사용자의 출생 연도를 입력 받아 나이를 출력하세요
# 만 나이 / 연 나이

birth_year=int(input("출생 연도 : "))
current_year=2026
age=current_year-birth_year
print("만 나이", age, "연 나이", age+1)