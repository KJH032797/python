# 자기소개 프로그램

'''
이름 :
나이:
키:
몸무게:

제 이름은 ㅇㅇㅇ이고,
나이는 ㅇㅇ살 입니다.
내년에는 ㅇㅇ살이 됩니다.
키랑 몸무게는 ㅇㅇ/ㅇㅇ입니다.
'''

name = input("enter your name:")
age = int(input("enter your age:"))
weight = float(input("enter your weight:"))
height = float(input("enter your height:"))

print(f"제 이름은 {name}이고,")
print(f"나이는 {age}살입니다.")
print(f"내년에는 {age+1}살이 됩니다.")
print(f"키랑 몸무게는 {height}/{weight}입니다.")
