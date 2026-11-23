number1 =float(input("enter the first number: "))
number2 =float(input("enter the second number: "))
operation = input("enter the operation you want to perform (+, -, *, / , % , ** , //): ")
if operation == '+':
    result = number1 + number2
    print (result)

elif operation == '-':
    result = number1 - number2
    print (result)

elif operation == '*':
    result = number1 * number2
    print (result)
elif operation == '/':
    result = number1 / number2
    print (result)

elif operation == '%':
    result = number1 % number2
    print (result)

elif operation == '**':
    result = number1 ** number2
    print (result)

elif operation == '//':
    result = number1 // number2
    print (result)

else:   print("invalid operation") 

# copyright @ sanyam soni ab