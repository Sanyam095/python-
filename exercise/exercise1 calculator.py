input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
operation = input("k krna h (plus, minus, multiply, divide): ")

if operation == "plus":
    result = input1 + input2
elif operation == "minus":
    result = input1 - input2
elif operation == "multiply":
    result = input1 * input2
elif operation == "divide":
    result = input1 / input2

print("Result:", result)
