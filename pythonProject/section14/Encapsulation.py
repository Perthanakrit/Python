class Animal:
    def eat(self):
        print("Eating")

class Cat(Animal):
    name = ""
    def setName(self,text):
        self.name = text
        print("Setting New cat Name=", self.name)

    def eat(self):
        print("Meow!")

cat1 = Cat()
cat1.setName("TT")

cat1.eat()
