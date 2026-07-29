# 동물과 이름 입력 후 출력

class Animal:
    def __init__(self, x, y): # 생성자
        self.name = x
        self.age = y

    def bark(self):
        print("짖는다")