# Dictionary is a combination of key and value pairs. It is a collection which is ordered, changeable and does not allow duplicates.
dic = {
    "Sanyam": "Human being",
    "Spoon": "Object"
}
print(dic["Sanyam"])
# to iska answer aayega "Human being"
dict ={
    344: "Harry",
    455: "Sanyam",
    678: "Neha",
    298: "Zakir"
}
print(dict[678])
# ab mujhe neha mil jaygi

# agr mujhe key words ki value dekhni h to do cheeje use hoti h 
# ek to normal vala
info = {'name': 'Sanyam', 'age': 20, 'eligible': True}
print(info['name'])
# iska answer aayega "Sanyam"
# aur ek get method hota h
print(info.get('name2'))
# iska answer aayega None kyuki name2 key exist nahi karti h
# agr krti to print ho jata
# lekin agr meine get nhi lgaya hota yanha to ye error throw krta 


# agr mujhe ek sath sari keys ko access krna h to mujhe aaise krunga
print(info.keys())

# ek cheej or ho skti h
for key in info.keys():
    print(info[key])
# agr mujhe sari values ko access krna h to aaise krunga
print(info.values())
# aur inke sath bhi same ho skta h



# for value in info.values():
#     print(info[value])



# m items bhi dekh skta hu 
print(info.items())
# aur inke sath bhi same ho skta h 
for key, value in info.items():
    print(f"The value corrosponding to the key {key} is {value}")