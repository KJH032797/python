# 사용자로부터 다음 정보를 입력받으세요.
# - 아이디
# - 비밀번호
# - 비밀번호 확인
# - 나이
# 다음 조건을 **모두 만족하는지** 출력하세요.
# - 아이디가 `"admin"`이 아님
# - 비밀번호와 비밀번호 확인이 같음
# - 나이가 14세 이상
# 예:
# 아이디: hong
# 비밀번호: 1234
# 비밀번호 확인: 1234
# 나이: 20
# 회원가입 가능: True

ID=input("아이디 : ")
password=input("비밀번호 : ")
password_check=input("비밀번호 확인 : ")
age=int(input("나이 : "))

a=ID!="admin"
b=password==password_check
c= age >= 14

terms=a and b and c

print(f"회원가입 가능 : {terms}")