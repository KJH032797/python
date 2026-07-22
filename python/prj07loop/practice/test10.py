# 자판기

menu = {"coke" : 1500, "soda" : 1300, "coffee" : 2000}
money = 10000
order = input()
s_money = 10000 - menu[order]

if order in menu:
    print(f"{menu[order]}원 차감되었습니다.")
    print(s_money)
    if s_money > 0:
        while s_money > 0:
        order = input()
        print(f"{menu[order]}원 차감되었습니다.")

