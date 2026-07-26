# 로또

import random

Lottery_start='''
==========로또 추첨을 시작합니다.===========
1부터 45까지 숫자 중에서 임의의 숫자 6개를 골라주세요.
추첨 숫자와 내가 고른 숫자가 몇 개 일치하는지에 따라
당첨 포인트가 달라지며 낙첨시 -2점 종료시에는 0점입니다.
종료를 원하시면 숫자 \"0\"을 입력하세요.
'''

# 당첨 이펙트 모음
EFFECT_1ST = """
  ★====================================★
          🏆 대 박 ! 1 등 당 첨 ! 🏆
          🎉 ! 추가 포인트 획득 ! 🎉
  ★====================================★
     \\ O /  축하합니다!
       |    로또 당첨 운을 여기에 쓰셨네요!
      / \\
"""

EFFECT_2ND = """
  ★====================================★
    🥈 2 등 당 첨 ! 축 하 합 니 다 ! 🥈
           ! 추가 포인트 획득 !
  ★====================================★
     거 봐! 따서 갚으면 되잖아!
"""

EFFECT_3RD = """
  --------------------------------------
    🥉 3 등 당 첨 ! 추가 포인트 획득 ! 🥉
  --------------------------------------
     아쉽게 1, 2등은 놓쳤지만 축하드려요!
"""

EFFECT_4TH = """
  --------------------------------------------------
    4 등 당 첨 ! ( 오늘은 김밥 대신 참치 김밥 정도는... )
  --------------------------------------------------
"""

EFFECT_5TH = """
  ------------------------------------------
           5 등 당 첨 ! ( 한 번 더 ? )
  ------------------------------------------
  다음엔 더 딸 수 있을 거 같은데...
"""

EFFECT_LOSE = """
  --------------------------------------
    😭 꽝 ! 아쉽게도 당첨되지 않았습니다.
  --------------------------------------
     다음 기회를 노려보세요!
"""



# 게임 함수
def Lotto():
    Lottery = range(1, 46)  # 로또 번호 범위
    w_number = random.sample(Lottery, 6)  # 당첨 번호
    user_numbers = [] # 사용자 선택 번호 리스트

    print(Lottery_start)
    print("로또 구매를 시작합니다.")

    # 번호 선택
    while len(user_numbers) < 6 :
        try:  # 번호 입력
            user_number = int(input(f"{len(user_numbers)+1} 번째 숫자를 입력하세요. : "))
        except ValueError: # 예외 처리
            print("숫자만 입력해주세요\n")
            continue

        if user_number == 0 : # 종료 처리
            print("게임을 종료합니다.")
            return 0

        if not (1 <= user_number <= 45) : # 예외 처리
            print("1부터 45까지의 숫자만 입력해주세요.")
            continue

        if user_number in user_numbers : # 예외 처리
            print("이미 선택한 숫자입니다. 다른 숫자를 입력해주세요.\n")
            continue

        user_numbers.append(user_number)

    print(f"\n[구매완료!] 선택하신 번호는 {user_numbers}입니다.")

    print("=" * 40)

    print("\n당첨 번호 추첨을 진행하시겠습니까? 종료하시려면 숫자 0, 진행하시려면 아무 키를 입력해주세요.")
    draw_start = input("진행하시겠습니까?\n")

    if draw_start == "0" : # 예외 처리
        print("\n게임을 종료합니다.")
        return 0
    else :
        print("추첨을 시작합니다. 아무 키를 입력해 번호를 하나씩 추첨해주세요.\n")

    # 번호 추첨
    for i, draw_num in enumerate(w_number, 1):
        input(f"[{i}번째 공 추첨...]")
        print(f"[{i}번째 당첨 번호는 {draw_num}번!]\n")

    print("=" * 40)

    print(f"[추첨 완료] 이번 로또 당첨 번호는 {w_number}입니다.")

    # 당첨 대조용
    purchase = set(user_numbers)
    winning_number = set(w_number)
    matched_numbers = purchase&winning_number
    matched_count = len(matched_numbers)

    input("당첨 확인을 진행하시려면 아무 키를 눌러주세요.\n")
    print(f"나의 번호 : {user_numbers}")
    print(f"일치 번호 : {matched_numbers}\n총 {matched_count}개 일치!")
    # 결과 확인
    if matched_count == 6 :
        print(EFFECT_1ST)
        print("\n당첨을 축하합니다. 게임을 종료합니다.")
        return 500
    elif matched_count == 5 :
        print(EFFECT_2ND)
        print("\n당첨을 축하합니다. 게임을 종료합니다.")
        return 200
    elif matched_count == 4 :
        print(EFFECT_3RD)
        print("\n당첨을 축하합니다. 게임을 종료합니다.")
        return 100
    elif matched_count == 3 :
        print(EFFECT_4TH)
        print("\n당첨을 축하합니다. 게임을 종료합니다.")
        return 10
    elif matched_count == 2 :
        print(EFFECT_5TH)
        print("\n당첨을 축하합니다. 게임을 종료합니다.")
        return 5
    else : # matched_count < 2
        print(EFFECT_LOSE)
        print("\n낙첨되었습니다. 게임을 종료합니다.")
        return -2