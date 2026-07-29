# 자판기

menu = {"콜라" : 1500, "사이다" : 1300, "커피" : 2000}
print(menu)
money = int(input("돈을 넣어주세요: "))


if money >= 1300 :
    while True :
        print(f"\n현재 잔액 {money}원")
        order = input("메뉴를 선택해주세요(종료를 원하면 \"종료\" 입력): ")
        if order in menu :
            if money >= menu[order]:
                money -= menu[order]
                print(f"{menu[order]}원 차감되었습니다.")

                if money < 1300:
                    print("\n잔액이 부족합니다. 이용해주셔서 감사합니다.")
                    print(f"거스름돈 : {money}원.")
                    break

            else :
                print("잔액이 부족합니다.")

        elif order == "종료" :
            print("\n이용해주셔서 감사합니다.")
            print(f"거스름돈 : {money}원.")
            break

        else :
            print("목록에 없는 메뉴입니다. 다시 입력해주세요.")

else :
    print("\n잔액이 부족합니다. 이용해주셔서 감사합니다.")
    print(f"거스름돈 : {money}원.")