# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contain at least 3 characters, remove the first letter and append it at the end
#  now append three random characters at the starting and the end 
# else:
# simply reverse the string 

# Decoding:
# if the word contains less than 33 characters, reverse it
# else:
# remove 3 random characters from the start and the end. Now remove the last letter and append it to the beginning

# Your programme should ask whether you want to code or decode


# ANSWER:
inp = input("What do you want exactly\n \t Code \t Decode\n Write here: ")
if (inp=="Decode"):
    data1 =input("Enter the word that you want to Deode: ")
    a = list(data1)
    print(a)
    if (len(a)<3):
        a.reverse()
        print(a.reverse)
    elif (a>=3):
        a.remove(len(0),len(1),len(2),len(a),len(a)-1,len(a)-2)
    else:
        raise ValueError("This word is not supported")
elif(inp=="Code"):
    data= input("Enter the word that you want to code: ")
    a = list(data)
    if (len(a) < 3):
        a.reverse()
        print(a)
    elif(len(a)>=3):
        a.append(a[0])
        a.remove(a[0])
        a.insert(0,"x")
        a.insert(0,"p")
        a.insert(0,"i")
        a.pop()
        a.pop()
        a.pop()
        print(a)
else:
    raise ValueError("This word is not supported!")