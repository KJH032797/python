import random

# 시작 안내문
UD_start = '''
==========업다운 게임을 시작합니다.===========
정답은 1부터 100 중에서 하나이며 기회는 6번이 주어집니다.
임의의 숫자를 하나 입력하여 시작하세요.
정답일 시 +1점, 기회 소진 혹은 자체 종료시 -1점이 됩니다.
종료를 원하시면 숫자 \"0\"을 입력하세요.
'''


# 업다운게임 함수
def UD() :
    answer = random.randint(1, 100) # 정답
    cnt = 6 # 기회
    print(UD_start)
    while True :
        print(f"{cnt}회 남았습니다.") # 남은 기회 수 안내
        try:
            n = int(input("숫자를 입력하세요. : ")) # 정답 입력
        except ValueError:
            print("숫자만 입력해주세요\n") # 예외 처리
            continue

        if n == 0 : # 종료 처리
            print("게임을 종료합니다.")
            return -1

        cnt -= 1 # 기회 차감
        # 정답 판별
        if answer > n:
            print("업!")

        elif answer < n:
            print("다운!")

        if answer == n and cnt > 0 :
            print("정답!")
            print("기회를 모두 소진하지 않고 맞췄습니다! 추가 포인트를 획득합니다.")
            return 3
        if answer == n and cnt == 0 :
            print("정답!")
            print("포인트를 획득하고 게임을 종료합니다.")
            return 1

        elif answer != n and cnt == 0 : # 기회 소진
            print("기회가 모두 소진되었습니다. 수고하셨습니다.")
            return -1