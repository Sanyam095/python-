a = int(input("Enter any value between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
else:
    print(a)


# a = str(input("Enter any value between 5 and 9: "))

# if (a !="quit"):
#     raise TypeError("This is not supported")
# else:
#     raise ValueError("This type of value is not supported")