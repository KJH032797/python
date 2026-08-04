from book import Book
import json


def write_to_file():
    with open("data.txt", "w",encoding="utf-8") as f:
        title=input("title : ")
        price=int(input("price : "))
        book=Book(title,price)
        json.dump(book.to_dict(), f, ensure_ascii=False, indent=2)

def read_from_file():
    with open("data.txt", "r",encoding="utf-8") as f:
        d = json.load(f)
        print(d)
        book = Book.from_dict(d)
        print(book.title)
        print(book.price)




while True:
    print("\n1. write")
    print("2. read")
    print("0. exit")
    num = int(input("\n실행할 메뉴 번호 : "))
    match num:
        case 0 :
            break
        case 1:
            write_to_file()
        case 2:
            read_from_file()



# with open("data.txt", "r", encoding="utf-8") as f:
#     for x in f:
#         print(x.strip())

# try :
#     f = open("data.txt", "a", encoding="utf-8")
#     f.write("\n계획하고 걱정않기")
# finally:
#     f.close()