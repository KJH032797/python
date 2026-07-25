# rules

# 시작 안내문
start = '''==========가위바위보 게임을 시작합니다.===========
승리시 +1점, 무승부시 0점, 패배시 -1점이 되며 총 10점이 되거나 5연승시에 최종 승리합니다.
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