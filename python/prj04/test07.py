# 비밀번호를 두 번 입력받고 두 값이 같은지 출력하세요.
# 비밀번호: python123
# 비밀번호 확인: python123
# True

비밀번호=input("please input your password : ")
비밀번호_확인=input("please retry input your password : ")
terms=비밀번호==비밀번호_확인

print(terms)