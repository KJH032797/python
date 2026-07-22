# up down game
# random
import random # 함수를 쓰기 전에 불러오기가 필요한 함수
answer=random.randint(1,100)
cnt=0

while True:
    n=int(input())
    cnt+=1
    if answer>n:
        print("up")
    elif answer<n :
        print("down")
    else:
        print("right")
        print(f"{cnt}번 만에 맞췄습니다.")
        break