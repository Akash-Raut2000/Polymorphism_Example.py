class Dog:
    def sound(self):
        return "Wooof"

class Cat:
    def sound(self):
        return "Meow"

for animal in(Dog(), Cat()):
    print(animal.sound())