class Poketmon :
    def __init__(self, a,b,c,d):
        self.name = a
        self.hp = b
        self.atk = c
        self.defe = d

    # def printInfo(self):
    #     data = self.getInfo()
    #     print(data)
    #     # print(self.name)
    #     # print(self.hp)
    #     # print(self.atk)

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"