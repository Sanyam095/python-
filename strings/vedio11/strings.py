name ="sanyam"
friend_name = "bhoomi"
# string ko hm single cotes ya double cotes me likh sakte hai

# multiline strings ko bnane ke liye hm triple cotes ka use karte hai
# ab vo cotes teri tehara single bhi ho skte h or uski tehara doubke bhi
string1 = """ he want to say that,
    he is a good boy
    and i am also a good boy"""
print(string1)

string2 = ''' he wants you 
not your pussy 
he wants your attention
not your body'''
print(string2)

# bhai m kuch aaisa bhi kr skta hu 
print(name[0]) # an name to sanyam h to sanyam ko 012345 me dekhta h python to 0 pr "s" h to "s" print ho jayga
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[4]) 
print(name[5]) 
# print(name[6]) yanha error aayga kyouki name me 6 index nahi h 

# ha agr mujhe sare character ek ek krke print krne h or string bhi bdi h 
# jaise string1 ya string2 to m for loop ka estemal krunga
for character in string1:
    print(character)