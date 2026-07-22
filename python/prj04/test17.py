# 회원 정보를 다음과 같이 저장했다고 가정합니다.
# user= ["kimgugbee","1234"]
# 사용자로부터 아이디와 비밀번호를 입력받아 **아이디와 비밀번호가 모두 일치하는지** 출력하세요.
# 아이디: kimgugbee
# 비밀번호: 1234
# 로그인 정보 일치: True

ID=input("ID : ")
password=int(input("password : "))

user_info=["kimgugbee",1234]

print(f"로그인 정보 일치 : {user_info[0]==ID and user_info[1]==password}")