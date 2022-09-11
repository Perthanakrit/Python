class Animal:
    def eat(self):
        print("Eating")

class Cat(Animal):
    def eat(self):
        print("Meow!")

cat1 = Cat()
cat1.eat()

animal1 = Animal()
animal1.eat()
