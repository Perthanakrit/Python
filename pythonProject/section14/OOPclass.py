class CustomerApp: #แบบแบลน
    name = ""   #Attribute
    lastName = ""
    age = 0

    def addcart(self):
        print("Added product to ", self.name, self.lastName, "'s cart")
        print(self.age)

customers1 = CustomerApp() #Object
customers1.name = 'Per'
customers1.lastName = "Trakanjan"
customers1.age = 10
customers1.addcart()

customers2 = CustomerApp()
customers2.name = "Goku"
customers2.lastName = "God"
customers2.age = 15
customers2.addcart()
