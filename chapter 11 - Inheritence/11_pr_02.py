class Animal:
    animalType = "Mammal"

class Pets(Animal):
    colour = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow !!")

d = Dog()
d.bark()