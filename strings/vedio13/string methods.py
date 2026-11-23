# Strings are immutable
a = "!!!!!sanyam!!!!  !!!!!!!sanyam"
print(len(a))
print(a)
print(a.upper()) # ye string ko upper case me convert kr dega---> yhi sbse bdi glt femi h 
# ye ek nyi string bna dega jo ki upper case me hogi
print(a.lower()) # similarly ye ek or nyi string bna dega jo ki lower case me h 
# kyouki jh mstring ko change nhi kr skte vo immutable h
# ye question interviews me aata h

# ab agr m chahata hu ki mere nam me se ye exlamation marks ht jay to m ye use krunga
print (a.rstrip("!")) # ye string me mere nam ki right side vale sare exlamation marks ko hta dega 
print (a.lstrip("!")) # ye string me mere nam ki left side vale sare exlamation marks ko hta dega 
print (a.strip("!")) # ye string me mere nam ki dono side vale sare exlamation marks ko hta dega 

# or agr mujhe apni string me kuch replace krna h to m ye use krunga
print(a.replace("sanyam", "harry")) # ye sanyam ko harry se replace kr dega 

# m string ko split bhi kr skta hu 
print(a.split( ))
# to ye string ko list bna dega or " " se split kr Dega
b ="sanyAm soNi"
# agr m b k phle letter ko capital me likhna chahata hu to bhi m kr skta hu
print(b)
print(b.capitalize())
# capitalize un gltiyo ko theek kr dega jaise meine abhi b string me a aur n ko capital likh diya tha to vo apne aap theek ho gye 
c = "Welcome to my home town"
print(c.center(50))
# iska mtlb ye center se 50 spacing pr print ho jayga
print(len(c))
print(len(c.center(50)))
# isne 25 spaces or add kr diye taki hmara text center ki trf move kr jay

# agr hme string me koi cheej count krni h k vo kitni bar aa rhi h to bhi hmare pass jugad h
print(a.count("!"))
# ab mujhe pta chal jayga ki meri string a me kitni bar ! h

#agr mujhe check krna ho ki meri string kisi cheej pr end ho rhi h ya nhi to uske liye bhi jugad h
print(a.endswith("!"))
# or meri string ! se end nhi ho rhi to mujhe false dikha agr hoti to true dikhta 
print(c.endswith("n"))
# or meri string c n k sath end ho rhi h to mujhe true dikha
# ye mujhe boolean data type dega jose m if else statements me bbhi use kr skta hu
print(c.endswith("to",4 ,10))
# ye btayega ki string c me 4th digit se 10th digit tk  ko ek string man le or kya vo to se end ho rhi h ya nhi hogi to true or nhi to false

# hm find bhi kr skte h kisi bhi cheej ko 
str1 = ("my he's name is sanyam")
print(str1.find("is"))
# ye btayega ki koi cheej aapki string me h ya nhi 
# agr h to ye uski index value de dega 
# or agr nhi h to uski value minus one de deta h, jaise
print(str1.find("ish"))
# iski value minus one -1 aayegi

# or agr tu sure h ki isme jo tu search krna chahata h vo h
# or agr na ho to tu chahata h ki ye error phek k mare 
# to ye use kr
print(str1.index("is")) # ye output dega
# or print(str1.index("ishh")) ye error phek k marega

# or hm ye bhi dekh skte h ki hmari string alpha numeric h ya nhi
#alpha numeric mtlb jo string a-z,A-Z,0-9 en aksharo se milkr bni ho
print(str1.isalnum())
# yanha output me false esiliye aaya kyouki ' ek alpha numerical key nhi h

# aaise hi hm ye bhi dekh skte h ki hmare string k sabhi words lower case me h ya nhi
print(str1.islower())
# aaise hi ek hota h upper case ko dekne k liye 

str2=("boy")
str3=("i am a boy\n")
# ye cheej check krti h ki aapki string me jo character h vo printable h ya nhi ,, mtlb koi escape sequence char too nhi h aapki string me
print(str2.isprintable()) # iska true aayega
print(str3.isprintable()) # iska fase aayega

# ek or hota h to ki dekhta h ki aapki string me space h ya nhi 
str4=("sanyamsoniji")
print(str3.isspace()) # true
print(str4.isspace()) # false
#ye frk nhi pdta ki spacing spacebaar se ya tab se hui h answer true hi aayega

# ek or hota h jisse hm pta kr skte h ki aapki string me hr ek word ka first letter capital h ya nhi 
str5 =("My Name Is Sanyam")
print(str5.istitle()) # true
print(str2.istitle()) #false
# hm title case me bna bhi skte h kisi bhi string ko
print(str2.title())

# aaise hi ek startwith bhi hota h jisse hm pta kr skte h ki jo hm keh rhe h us word se aapki string chalu ho rhi h ya nhi
print(str5.startswith("My")) # true
print(str5.startswith("name")) # false

# ek or hota h jo lower case ko upper case or upper case ko lower case me convert kr deta h
print(str5.swapcase())