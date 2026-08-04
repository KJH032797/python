import json
from model.ToDo import ToDo

ToDo_list = []

# json ===========================================================

def save_list(): # 기존 ToDo에서 입력된 데이터를 json에 저장
    dict_list = []
    for td in ToDo_list:
        dict_list.append(td.to_dict())

    with open("book_data.json", "w", encoding="utf-8") as f:
        json.dump(dict_list, f, ensure_ascii=False, indent=2)

def load_list(): # json에 저장된 데이터를 ToDo_list에 다시 불러와 활용
    try:
        with open("book_data.json", "r", encoding="utf-8") as f:
            dict_list = json.load(f)
            ToDo_list.clear()
            for dict_data in dict_list:
                ToDo_list.append(ToDo.from_dict(dict_data))
    except Exception as e:
        print(type(e))
        print(e)
        pass


# 기존 Todo 기능 구현 ==============================================

def print_menu():  # 목록 출력
    print(
        "\n----- menu -----\n"
        "1. 할 일 추가\n"
        "2. 목록 보기/관리\n"
        "0. 종료\n"
    )


def scan_user_input():  # 목록 선택
    while True:
        try:
            return int(input("Enter menu number: "))
        except Exception as e:
            print(type(e))
            print(e)
            print("숫자로만 입력해주세요.\n")


def process(num): # 목록 실행
    match num:
        case 1:
            add_work()
        case 2:
            show_list_and_manage()


# 우선 순위
def get_priority(td):
    return td.priority


# 할 일 추가
def add_work():
    print(
        "\n----- Add work -----\n"
        "할 일의 이름과 내용을 입력하고 우선 순위를 중요도에 따라 숫자를 입력하세요")
    n = input("이름 : ").strip()
    c = input("내용 : ").strip()
    while True:
        try:
            p = int(input("우선 순위 : "))
            break
        except Exception as e:
            print(type(e))
            print(e)
            print("숫자로만 입력해주세요.\n")

    td = ToDo(name=n, content=c, priority=p)
    ToDo_list.append(td)
    ToDo_list.sort(key=get_priority) # 우선 순위 정렬

    save_list() # 입력된 데이터를 저장
    print("등 록 완 료 !\n")


# 상세 보기 및 편집
def show_list_and_manage():
    # 목록 보기
    if not ToDo_list:
        print("\n할 일이 없습니다. 뭐하지...\n")
        return

    print("\n----- To Do List -----\n")
    for i, show in enumerate(ToDo_list):
        if show.done:
            status = "[V]"
        else:
            status = "[ ]"
        print(f"{status} | {i}. {show.name}")

    # 작업 선택
    print("\n[ 작업 선택 ]")
    print(
        "1. 완료 상태 변경 | 2. 상세 보기 | 3. 삭제 | 0. 돌아가기"
    )

    while True: # 예외 처리
        try:
            answer = int(input("선택 : "))
            if 0 <= answer <= 3:
                break
            else:
                print("올바른 번호를 입력해주세요.\n")
        except Exception as e:
            print(type(e))
            print(e)
            print("숫자로만 입력해주세요.\n")

    match answer: # 실행
        case 0:
            return
        case 1: # 상태 변경
            target, num = select_item()
            if target:
                toggle_done(target)
        case 2: # 상세 보기 및 수정
            target, num = select_item()
            if target :
                detail(target)
                print("\n1. 내용 수정 | 2. 삭제 | 0. 돌아가기")

                while True:
                    try:
                        choice = int(input("해당 목록을 수정하시겠습니까? : "))
                        if 0 <= choice <= 2:
                            break
                        else:
                            print("올바른 번호를 입력해주세요.\n")
                    except Exception as e:
                        print(type(e))
                        print(e)
                        print("숫자로만 입력해주세요.\n")
                if choice == 1:
                    edit(target)
                elif choice == 2:
                    delete_item(num)
        case 3: # 삭제
            target, num = select_item()
            if num is not None:
                delete_item(num)


# target/num 값 반환
def select_item():
    if not ToDo_list:
        return None, None

    while True:
        try:
            num = int(input("\n목록 번호를 선택하세요(-1 입력 시 취소) : "))
            if num == -1:
                print("취소되었습니다.\n")
                return None, None
            if 0 <= num < len(ToDo_list):
                target = ToDo_list[num]
                return target, num
            else:
                print("목록에 없는 번호입니다.")
        except Exception as e:
            print(type(e))
            print(e)
            print("숫자로만 입력해주세요.\n")


# 상세 보기
def detail(target):
    print("\n----- 상세 정보 -----")
    print(target)


# 완료 상태 변경
def toggle_done(target):
    target.done = not target.done
    if target.done:
        status_str = "완료"
    else:
        status_str = "미완료"

    save_list()
    print(f"상태가 [{status_str}](으)로 변경되었습니다 !\n")


# 편집
def edit(target):
    print(
        "\n1. 이름 | 2. 내용 | 3. 우선순위 | 4. 완료 상태 변경\n"
    )

    while True:
        try:
            num = int(input("수정할 항목을 선택해주세요 : "))
            if 1 <= num <= 4:
                break
            else:
                print("올바른 번호를 입력해주세요.\n")
        except Exception as e:
            print(type(e))
            print(e)
            print("숫자로만 입력해주세요.")

    match num:
        case 1:
            target.name = input("이름 편집 : ").strip()
            save_list()
            print("수 정 완 료 !\n")

        case 2:
            target.content = input("내용 편집 : ").strip()
            save_list()
            print("수 정 완 료 !\n")

        case 3:
            while True:
                try:
                    target.priority = int(input("우선 순위 편집 : "))
                    ToDo_list.sort(key=get_priority)
                    save_list()
                    print("수 정 완 료 !\n")
                    break
                except Exception as e:
                    print(type(e))
                    print(e)
                    print("숫자로만 입력해주세요.\n")
        case 4:
            toggle_done(target)

# 삭제
def delete_item(num):
    while True:
        delete = input("\n이 항목을 삭제하시겠습니까? (Y/N)").strip().upper()
        if delete == "Y":
            del ToDo_list[num]
            save_list()
            print("삭 제 완 료 !\n")
            break
        elif delete == "N":
            print("메뉴로 돌아갑니다.\n")
            break
        else:
            print("Y or N 으로만 대답해주세요.\n")