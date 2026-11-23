int('''There are two thing that my store have at this time
      Chocolate = 10Rs
      spicychips = 100Rs''')
chocolate = 10
spicychips = 100
budget = float(input(("So kindly enter your budget in Rs: ")))

if (budget< 10):
    print("You are not able to buy any thing")
elif (budget >=10 and budget <100):
    print("Your bill is 10 Rs ", "\n you buy chocolate successfully","\n you have",budget-10," rs left")
elif (budget >=100 and budget <110):
    print("Your bill is 100 Rs","\nyou buy spicy chips successfully","\n you have",budget-100," rs left")
else:
    print("your bill is 110 Rs","\nyou buy spicy chips and chocolate successfully","\n you have",budget-110," rs left")