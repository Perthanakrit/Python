class Vehicle: #แม่แบบ
    licenseCode = ""
    seriaLCode = ""
    def turnOnaircondition(self):
        print("Trun on:Air")
class Car(Vehicle):
    pass
class PickUp_Car(Vehicle):
    def sayhello(self):
        print("Hello world")
class van(Vehicle) :
    pass

car1 = Car()
car1.turnOnaircondition()
Pickup1 = PickUp_Car()
Pickup1.turnOnaircondition()
Pickup1.sayhello()
