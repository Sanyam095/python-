a = True
print(a:=False) # iska mtlb ye hai ki m a ko phle false bna rha hu or bad mr print kr rha hu 

# another example
numbers = [1, 2, 3, 4, 5]
while (n := (len(numbers))) > 0:
    print(numbers.pop())

# another one
happy = False
print(happy :=True)

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
