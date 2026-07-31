from model.book import Book

book_list = []

# print_menu
def print_menu():
    print("---- menu ----"
          "\n0. 프로그램 종료"
          "\n1. 도서 등록"
          "\n2. 도서 목록"
          "\n3. 도서 조회"
          "\n4. 도서 삭제")

# scan_user_input
def scan_user_input():
    return int(input("메뉴 번호 : "))

#process
def process(num):
    match num:
        case 0:
            return
        case 1 :
            enroll_book()
        case 2 :
            select_book_list()
        case 3 :
            select_book_one()
        case 4 :
            remove_book()

# 등록
def enroll_book():
    print("---- 도서 등록 ----")
    t = input("title : ")
    a= input("author : ")
    book = Book(title=t, author=a)
    book_list.append(book)
    print("도서 등록 완료 !")

# 목록조회
def select_book_list():
    print(" ---- 도서 목록 ---- ")
    for i, book in enumerate(book_list):
        print(f"{i}. {book.title}")

# 상세조회
def select_book_one():
    print("---- 도서 상세 ----")
    num = int(input("도서 목록 번호 입력 : "))
    book = book_list[num]
    print(book)

# 삭제
def remove_book():
    print("---- 도서 삭제 ----")
    num = int(input("도서 목록 번호 입력 : "))
    del book_list[num]
    print("삭제 완료 !")