double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y : (x+y)/2

print(double(5))  
print(cube(5))
print(avg(5, 10))

# bhai m function ko bhi function pass kr skte h 
def appl(fx , value):
    return 6 + fx(value)
print(appl(cube, 2))

# bhai jyadatr lambda function ka use kuch aaise hota h 
print(appl(lambda x: x+3, 5))