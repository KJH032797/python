import random
from abc import abstractmethod, ABC


class Poketmon(ABC):
    def __init__(self, name, max_hp, atk, arm):
        self.name = name
        self.max_hp = max_hp
        self.max_hp = min(self.max_hp, max_hp)
        self.hp = max_hp
        self.hp = max(self.hp, 0)
        self.atk = atk
        self.arm = arm
        self.is_stunned = False
        self.is_burned = False
        self.is_defensed = False

    def __str__(self):
        return f"{self.name} ({self.hp}/{self.max_hp})"

    def tackle(self, enemy):
        print("\n몸 통 박 치 기 ! ! !")
        dmg = self.atk - enemy.arm
        max(dmg, 1)
        enemy.hp -= dmg
    @abstractmethod
    def skill(self, enemy):
        pass

    def is_dead(self):
        return self.hp <= 0


class Pikachu(Poketmon):
    def __init__(self):
        super().__init__("피카츄", 100, 5, 3)

    def skill(self, enemy):
        print("\n100 만 볼 트 ! ! !")
        dmg = random.randint(7, 30) - enemy.arm
        enemy.hp -= dmg
        if random.random() < 0.3 :
            enemy.is_stunned = True
            print(f"{enemy.name}가 감전되었습니다!")



class Lizard(Poketmon):
    def __init__(self):
        super().__init__("파이리", 90, 8, 3)

    def skill(self, enemy): # 턴제 개념시 지속 dmg
        print("\n불 꽃 세 례 ! ! !")
        dmg = self.atk - enemy.arm
        enemy.hp -= dmg
        enemy.is_burned = True


class Turtle(Poketmon):
    def __init__(self):
        super().__init__("꼬부기", 110, 3, 6)

    def skill(self, enemy):
        print("\n물 대 포 ! ! !")
        dmg = self.atk * 2 - enemy.arm
        enemy.hp -= dmg
        self.hp += round(dmg * 0.3, 0)