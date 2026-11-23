class Math:
    def __init__(self, num):
        self.num =  num

    def addtonum(self,n):
        self.num = self.num +n

    @staticmethod
    def add(a,b): # dekh ye class k andr h to m ise class k nam se bhi call kr skta hu or m ise normal fuction k nam se bhi call kr skta hu or mujhe self arguement dene ki jrurt bhi nhi pdi
        return a + b

# result = Math.add(1, 2)
# print(result) # output 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(7, 2))
print(Math.add(7, 2))

# ek important interciew ka ques hai
# Ques:
# kya hme ek class k andr method bnane k liye self arguement dena jruri hai 
# Answer:
# nhi, bilkul jruri nhi hai