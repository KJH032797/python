class Pikachu:
    def __init__(self):
        self.name = "Pikachu"
        self.hp = 75
        self.atk = 20
        self.defe = 2

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk} {self.defe}"