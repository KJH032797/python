class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self):
        print(f"{self.name} has {self.hp} hp {self.atk} atk")

    def attack (self, attacker, target):
        print(f"{attacker.name} attacked {target.name}")
        target.hp -= self.atk
        print(f"{target.name} left {target.hp} hp")

    def is_alive(self):
        if self.hp > 0 :
            return True

        elif self.hp <= 0:
            return False

class player(Hero):
    def __init__(self) :
        super().__init__("player", 100, 25)

class monster(Hero):
    def __init__(self) :
        super().__init__("monster", 80, 15)