class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


# 이 파일을 직접 실행할 때만 동작하기
# 다른 파일이 import하는 과정에서 실행 x
# print("__name__ : ", __name__)
# if __name__ == 'model.book' :
#     print('''book file''')