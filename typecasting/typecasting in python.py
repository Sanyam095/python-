#pehli bat ki hm  string k ander no bhi dal skte h 
a = "1"
b = "2"
print(a+b) 
#yeh dono string ko jod dega aur 12 print hoga
# jadu
c = "Sanyam"
d =" bhai"
print(c+d)
# aaise bhi kr skte h
# typecasting hoti kya h
# kisi ek data type ko dusre data type me convert krne ko typecasting kehte h
# ab jaise ki a = 1 tha 
# or b = 2 tha
print(int(a)+int(b)) # agr m aaise krunga to chalega 
print(a+b) # agr m aaise krunga to bhi chalega lekin string k systum se chalega
# typecasting k do type hote h 
# explicit or implicit

# explicit typecasting me hm khud se data type ko convert krte h
# jaise ki abhi print(int(a)+int(b)) me hm khud se int me convert kr rha hu

# implicit typecasting me python khud se data type ko convert kr deta h automatically jaise
x=5
y=2.5
z = x+y
print(x+y) # yaha python khud se x ko float me convert kr dega or fir add kr dega
type(z) # yaha z ka type float hoga kyuki python ne x ko float me convert kr diya tha