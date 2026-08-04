from List_manager import print_menu, scan_user_input, process

print("===== To-Do Manger =====")

while True:
    try :
        print_menu()
        num = scan_user_input()
        if num == 0 :
            print("프로그램을 종료합니다.")
            break
        process(num)
    except Exception as e :
        print(type(e))
        print(e)
        print("올바른 값을 입력해주세요")