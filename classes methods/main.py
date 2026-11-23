class employee:
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

    @classmethod # ye class variable ko hi change kr dega.......
    def changeCompany(cls , newCompany):
        cls.company = newCompany


e1 = employee()
e1.name = "Harry"
e1.changeCompany("Tesla")
e1.show()
print(employee.company)
