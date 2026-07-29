import random
from game.kh import judgeUpDown as abc

print("=====UP DOWN GAME=====")

# 정답(랜덤)숫자 준비하기
answer = random.randint(1, 100)

while True :
    # 유저한테 입력받기
    num = int(input("정답은 : "))
    # 판단하기 + 결과 출력
    result = abc(answer, num)
    print(result)
    if result :
        break