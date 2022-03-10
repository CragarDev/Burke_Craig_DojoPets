from pets import Pet
from tricks import Tricks
from pets import Dog

print("")
"""
# n-  Craig Burke Assignment - Dojo Pets
? Assignment: Dojo Pets

Objectives
More practice with OOP and class association.


Ninja Class

Attributes

first_name
last_name
pet
treats
pet_food


Methods

walk()
feed()
bathe()

// Create a Ninja class with the ninja attributes listed above.

// Create a Pet class with the pet attributes listed above.

// Implement walk(), feed(), bathe() on the ninja class.

// Implement sleep(), eat(), play(), noise() methods on the pet class.

// Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.

// Have the Ninja feed, walk , and bathe their pet.

// NINJA BONUS: Use modules to separate out the classes into different files.

t- SENSEI BONUS: Use Inheritance to create sub classes of pets.

Compress or zip up assignment and upload it.

"""


class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        if data["pet_name"] != "none":
            self.treats = data["treats"]
            self.pet_food = data["pet_food"]
            self.pet_name = data["pet_name"]
            self.pet_type = data["pet_type"]
            self.pet_tricks = data["pet_tricks"]
            self.pet = Pet(self.pet_name, self.pet_type, self.pet_tricks)
        else:
            self.pet = "none"
            self.pet_name = "none"

    # implement the following methods:

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        if self.pet == "none":
            self.noPet(self)
            return self
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if self.pet == "none":
            self.noPet(self)
            return self
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        if self.pet == "none":
            self.noPet(self)
            return self
        self.pet.noise()
        self.pet.sleep()
        return self

    def displayNinja(self):
        print(f"Name: {self.first_name} {self.last_name}")
        if self.pet_name != "none":
            print(f"Pet Name: {self.pet_name}")
            print(f"Pet Type: {self.pet_type}")
            print(f"Pet Food: {self.pet_food}")
            print("Pet Tricks: ")
            for trick in self.pet_tricks:
                print(f"   {trick}")
            print(f"Health: {self.pet.health}")
            print(f"Energy: {self.pet.energy}")
        else:
            print("No pets")
        return self

    @staticmethod
    def noPet(self):
        print("You don't have a pet!")
        print("")
        return self


nagotoT_data = {
    "first_name": "Tony",
    "last_name": "Nagoto",
    "treats": "Milky Bones",
    "pet_food": "Pet-Salmon Grand",
    "pet_name": "Wolfy",
    "pet_type": "German Sheppard",
    "eye_color": "blue",
    "breed": "Sheppard",
    "pet_tricks": ["Sit", "Stay", "Fetch"]
}


pepper = Dog(nagotoT_data)
print(pepper.breed)
pepper.perform_trick("Roll Over")
pepper.eat()
print("")
nagotoT = Ninja(nagotoT_data)

nagotoT.displayNinja()
print("")
nagotoT.bathe()
nagotoT.walk()
nagotoT.feed()
nagotoT.pet.eat()

nagotoT.displayNinja()
print("")


tim_data = {
    "first_name": "Tim",
    "last_name": "Tin",
    "treats": "DentaSticks",
    "pet_food": "Wagon Cart",
    "pet_name": "Barf",
    "pet_type": "Boxer",
    "pet_tricks": ["Stand", "Run", "Bark"]
}

tim = Ninja(tim_data)

tim.displayNinja()
print("")
tim.bathe()
tim.walk()
tim.feed()
tim.displayNinja()
print("")


sandy_data = {
    "first_name": "Sandra",
    "last_name": "Taylor",
    "pet_name": "none",
}

sandy = Ninja(sandy_data)

sandy.displayNinja()
print("")
sandy.bathe()
# print(sandy.pet)
sandy.displayNinja()
print("")


#  Just incase it doesn't work
""" 

"""
