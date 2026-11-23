x = 10  # ye ek global variable ho gya

def hello():
    x = 5  # ye ek local variable ho gya
    print(f"The value of local x is {x}")
    print(x)

hello()
print(x)
print(f"The value of global x is {x}")

# agr m global variable ko change krna chahata hu kisi bhi function k threw to mujhe bs global keyword ka use krna hoga
def change_global():
    global x  # ye global variable ko refer kr rha hai
    x = 20  # ab global variable change ho gya
    print(f"The value of changed global x is {x}")

change_global()
print(f"The value of global x is {x}")
# le ho gya change