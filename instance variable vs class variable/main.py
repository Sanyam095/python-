class employee:
    companyName = "Apple"
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raiseamount = 0.02
        employee.noOfEmployee += 1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raiseamount}")

emp1 = employee("Harry")
emp1.raiseamount = 0.06
emp1.companyName = "Apple India" # kyuki harry k case me instance variabel mojud tha to vo show hua 
emp1.showdetails()
# employee.showdetails(emp1)

employee.companyName = "Google"

emp2 = employee("Rohan") # lekin rohan k case me koi instance variable nhi tha companyName nam ka to class variable show ho gya
emp2.showdetails()

# ynha companyName class variable hai or raise amount name vgra instance variables hai
print(employee.companyName)
# mtlb change to class variable ko bhi kr skte ho aap