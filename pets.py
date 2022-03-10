
""" 
Pet Class

Attributes

name
type
tricks
health
energy

"""


class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks="none"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print("I'm Full....")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print("Bark meow hissss......")
        return self


class Dog(Pet):
    def __init__(self, data):
        super().__init__()
        self.breed = data["breed"]
        self.eye_color = data["eye_color"]

    def perform_trick(self, trick):
        print(f"I have performed '{trick}'")
