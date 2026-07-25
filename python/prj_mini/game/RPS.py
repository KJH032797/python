import random

# rules

# 시작 안내문
start = '''
==========가위바위보 게임을 시작합니다.===========
승리시 +1점, 무승부시 0점, 패배 혹은 자체 종료시 -1점이 되며 총 5점이 되거나 3연승시에 최종 승리합니다.
가위, 바위, 보 중에 하나를 입력하세요. 종료를 원하시면 \"종료\"를 입력하세요.
'''

rsp_list = ["가위", "바위", "보"] # 컴퓨터 선택지

# 승패 판정
def check(user_shot, computer_shot):
    win1 = user_shot == "가위" and computer_shot == "보"
    win2 = user_shot == "바위" and computer_shot == "가위"
    win3 = user_shot == "보" and computer_shot == "바위"

    if win1 or win2 or win3:
        return "win"
    if user_shot == computer_shot:
        return "draw"
    else :
        return "lose"


# 가위바위보 함수
def RPS() :
    user_cnt = 0 # 사용자 점수
    user_win = 0 # 사용자 연승 횟수
    com_cnt = 0 # 컴퓨터 점수
    com_win = 0 # 컴퓨터 연승 횟수
    print(start)
    while True:
        print("\n가위, 바위, 보!")
        user_shot = input("user : ").strip()

        if user_shot == "종료" : # 종료 처리
            print("\n게임을 종료합니다. 수고하셨습니다.\n")
            return -1

        if user_shot not in rsp_list : # 입력 예외 처리
            print("가위, 바위, 보 중에서만 입력해주세요.")
            continue

        computer_shot = random.choice(rsp_list)
        print(f"com : {computer_shot}")

        result = check(user_shot, computer_shot) # 승패 판정

        if result == "draw": # 무승부
            user_win = 0
            com_win = 0
            print("무승부!")
            print(f"user 승점 : {user_cnt}\n컴퓨터의 승점 : {com_cnt}")

        elif result == "win": # 사용자 승리
            user_cnt += 1
            user_win += 1
            com_cnt = max(0, com_cnt -1)
            com_win = 0
            if user_win >= 2:
                print(f"{user_win}연승!")

            else:
                print("승리!")

            print(f"user 승점 : {user_cnt}\n컴퓨터의 승점 : {com_cnt}")

            if user_cnt == 5 and user_win != 3:
                print("\n최종 승리하셨습니다. 축하합니다!\n")
                return 1

            if user_win == 3 :
                print("\n최종 승리하셨습니다. 축하합니다!\n")
                return 3

        elif result == "lose" : # 컴퓨터 승리
            user_cnt = max(0, user_cnt -1)
            user_win = 0
            com_cnt += 1
            com_win += 1

            if com_win >= 2 :
                print(f"컴퓨터의 {com_win}연승!")

            else:
                print("컴퓨터의 승리!")

            print(f"user 승점 : {user_cnt}\n컴퓨터의 승점 : {com_cnt}")

            if com_cnt == 5 or com_win == 3 :
                print("\n컴퓨터가 최종 승리하였습니다. 수고하셨습니다.\n")
                return -1