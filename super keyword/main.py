class parentClass:
    def parentMethod(self):
        print("This is a parent method.")

class childClass(parentClass):
    # def parentMethod(self):
    #     print("Harry")
    #     super().parentMethod()

    def childMethod(self):
        print("This is a child method.")
        super().parentMethod()

childObject = childClass()
childObject.childMethod()
childObject.parentMethod()
# childObject.parentMethod() ab uper vala run hoga kyuki childclass parentclass ka baccha hai or use parentclass ka method virasat me mila hai
# mtlb agr childclass k pass apna khud ka method hai to vo apne method ko hi run krega nhi to vo parent class ka method run kr dega


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
rohan = employee("Rohan", 1)
harry = programmer("Harry", 2, "Python")
print(rohan.name)
print(harry.name)
# superrrrrrrrrrrrrr................   frankeyyyyyyyyyyyyyyyyyyyyyyy................
