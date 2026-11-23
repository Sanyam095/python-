class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "Harry-12000"

e2 = employee.fromstr(string)
print(e2.name)
print(e2.salary)

# bhai string.split("-") se string split ho jaygi jnha jnha - hai or vo ek list bn jaygi jisme strings entries hai.
# jaise isme hi dekhle:
# string = "Harry-12000" thi phle or jb meine string.split("-") kiya:
# # to ye list ban gayi: ['Harry', '12000']
