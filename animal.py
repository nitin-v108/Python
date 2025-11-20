class Animal:
    def sound(self):
        print("Some Sound")

class Dog(Animal):
    def sound(self):
        print("Boww!")

d = Dog()
d.sound()