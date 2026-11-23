class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"The name of employee {self.id} is {self.name}")

class programmer(employee):
    def showlanguage(self):
        print("This is a programmer but you are a bloody fucking brat who is watching this masterpiece")

e1 = employee("sanyam", 100)
e1.showdetails()
e2 = programmer("aman", 290)
e2.showlanguage()