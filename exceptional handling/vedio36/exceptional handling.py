# exception handling me aaisa krna hota h ki agr mera program ache se run ho rha h to run ho jay or agr koi error aata h to kuch or ho jay
a = input("Enter the number: ")
try:
    a = int(a)
    print(f"Multiplication table of {a} is: ")
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Please enter a valid integer.")  

print("Some important lines of code")
print("The program is ended.")
# ab agr m try statement ka use nhi krta to error aane ka chance hota or ye imp lines of code run nhi hoti 
# but ab ye run ho jayengi chahe error aaye ya nhi aaye

# m jis type k error ko handle krna chahu us type k error ko handle kr skta hu
try:
    num =int(input("Enter an integer: "))
    a =[6, 3]
    print(a[num])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index Error")