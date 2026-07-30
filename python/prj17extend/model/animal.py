from abc import abstractmethod


class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} {self.category}"

    @abstractmethod
    def sounds(self):
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "mammals")

    def sounds(self):
        print("bowwow")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "mammals")

    def sounds(self):
        print("meow")

class Sparrow(Animal):
    def __init__(self):
        super().__init__("Bird", "birds")

    def sounds(self):
        print("tweet")

class Squirrel(Animal):
    def __init__(self):
        super().__init__("Squirrel", "rodents")

    # def sounds(self):
    #     print("peeps")