class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class dancerEmployee(employee ,dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

class dancerEmployee2(dancer, employee):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

o = dancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()


o2 = dancerEmployee2("Kathak", "Shivani")
o2.show()
# mtlb agr meine dancerEmployee class me phle dancer likhunga or bad me employee likhunga or ek aaisa method call krunga jo dono me hai to phle vale ka method call kiya jayga.
print(dancerEmployee.mro())
print(dancerEmployee2.mro())