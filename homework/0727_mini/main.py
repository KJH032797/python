from RPS import RPS
from updown import UpDown
from Lotto import Lotto

welcome='''시작 포인트 1점이 지급되었습니다.
게임을 선택하면 승패에 따라 포인트가 차감 또는 추가 됩니다.
종료 혹은 원하시는 게임의 번호를 입력해주세요.
'''


game_list='''1. 가위바위보
2. 업다운
3. 로또
4. 행맨
5. 타자연습
0. 종료'''

user_point = 1
game_number={1:RPS, 2:UpDown, 3:Lotto}

print(welcome)

while user_point > 0 :
    print(game_list)
    try:
        user_choice = int(input("번호를 입력해주세요 : "))
    except ValueError:
        print("올바른 번호를 입력해주세요\n")
        continue

    if user_choice not in game_number and user_choice != 0:
        print("올바른 번호를 입력해주세요\n")
        continue

    if user_choice == 0:
        print("\n게임을 종료합니다. 이용해주셔서 감사합니다.")
        break

    result_point = game_number[user_choice]()
    user_point += result_point

    print(f"현재 포인트 : {user_point}\n")

if user_point <= 0 :
    print("포인트가 부족하여 게임을 진행할 수 없습니다. 이용해주셔서 감사합니다.")