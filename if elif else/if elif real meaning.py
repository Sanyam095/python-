num = int(input("Enter the value of num: "))
# yanha se number ka input lunga

if (num < 0):   # sbse phle iske pas jayga python ki meri condition met kra de 
    print("Number is negative.") # hui to bs ye hi print hoga nhi to agle vale ko pass hoga 
elif (num == 0):  # fir second no iska aayega 
    print("Number is Zero.") # iski condition met hi to bs ye hi print hoga 
elif(num == 999): # fir third no iska aayega
    print("Number is special") # iski conditions met hui to yhi print hoga bs fir chahe aage kisi or ki bhi met hoti rhe 
else: # jo pehle aayega vo pehle payga or fir fourth no iska aayega
    print("Number is positive.") # iski condition met hui to ye print ho jayga
 # or ye to alg level ka aadmi h 
print("I am happy now") # ye to print hoga hi hoga kyouki ye if elif else ki ladder se bhar h
# mtlb ye sukh dukh or duniya se pre h shanti me

# range k third number ka mtlb
for i in range(0,101,20):
    print(i,end=",")
# ye loop 0 se start hoga or 100 tk jayga 
# lekkin 20-20 k gap me
# output= 0,20,40,60,80,100