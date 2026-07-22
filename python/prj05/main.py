#제어문

# if조건식 :
# 실행코드
# 실행코드
# 실행코드

# elif조건식 :
# 실행코드
# 실행코드
# 실행코드

# else :
# 실행코드
# 실행코드
# 실행코드

#if

time1=int(input("출발시간 : "))
time2=int(input("이동시간 : "))

time3=time1+time2
print(f"도착시간 : {time3}")

time4=int(input("약속시간 : "))

if time3>time4:
    print("late")
else:
    print("safe")
