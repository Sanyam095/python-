## list ko kyu use krte h hm 
# taki hm ek hi entity me bhot sara data store kr ske
# list are ordered collection of data
marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0]) # yanha mujhe bs 0th no wala element dekhne ko milega list ka jo ki 3 h is casse me
print(marks[1]) # similarly yanha 5
print(marks[2]) # or yanha 2
# ek list k ander ek se jyada data types bhi bhar skte h hm 
# jaise 
list = [90, 39, 82,"Sanyam","Bhoomi",True,["Pink","Red","Blue"]]
## Is list ki length 7 h lekin index 6 h 
# meine is list me numbers string boolen and even list sare data types bhar diye h 
# or list bhai sahab ko koi dikkat nhi h 
print(list[6])

print(marks[-3]) # Negative index
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])
# to print 6 hoga kyouki uska index 2 h beshak vo 3rd no pr ho 
# to kvi khna chahata h ki tumhe khi bhi negative indexing dikh jaye to use tum positive index me convert kr lo 
# tumhara kam ho jayga

# agr mujh pta krna h ki koi ek element list me h ya nhi 
if 6 in marks:
    print("Yes")
else:
    print("No")
# iska answer yes aayega
### agr m "6" ko as a string dal deta to mujhe no milta 
if "Sanyam" in marks:
    print("Yes")
else:
    print("No")
# or iska no
# m string k sath bhi ye if else vale kand kr skta hu 
if "yam" in "Sanyam":
    print("Yes")
else:
    print("No")
# iska answer yes aayega
if "sam" in "Sanyam":
    print("Yes")
else:
    print("No")
# or iska no

# hm slicing bhi kr skte h 
print(list)
print(list[1:-1])
# iska mtlb print(list[1:4])
# m slicing k sath jumping bhi kr skta hu
# jump index ka use krke
list2 =[1,2,3,4,5,"Sanyam","Bhoomi","Harry",True,False]
print(len(list2))
print(list2[1:9:2])
# iska mtlb 1 se 9 tk slicing kr dega 
# or fir 2-1 yani 1 element ka jump lega