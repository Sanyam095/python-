def average(a=9,b=1):
    print("The average is ",(a+b)/2)
# ab mujhe kuch bhi krna hoga to m seedha aise kr dunga
average()
average(a=2,b=2)
# m chahu to kisi ek ki value dekr dusre ki predefined bhi rakh skta hu
average(a=4)
average(b=0)
# agr hm chahete h ki order matter na kre to hm kuch aaise bhi kr skte h
average(b=3,a=0)
# isme order matter nhi krega

## Required arguements 
# ye aaise arguements hote h jinki value hme deni hi pdti h
def gmean(a,b=0):
    print("The arithmetic mean is:",gmean)
# yanha meine b ki value to pre defined kr di lekin a ki nhi ki h 
# to jb bhi m gmean ka prayog krunga tb tb mujhe a ki value to deni hi Pdegi
# ha b ki value ki meri mrji h ki du ya na du


# ek mst cheej mili h bhai
# esse m kitne bhi numbers ka average nikal skta hu
# or yad rakhna ki * lgane se ye value touple me deta h 
def averageadv(*numbers):
    print(type(numbers)) # ye tuple me le lega
    sum=0
    for i in numbers:
        sum = sum + i 
    print("Average is: ", sum/len(numbers))
# ab dekh tu systum
averageadv(1,3,5,6,7,7,8,0)
# m yanha kitne bhi numbers kr skta hu sbka average de dega ye 

## or agr hm double star lga denge to ye dictionary me le leta h
def insta(**name):
    print(type(name)) # class to iski dictionary rhegi
    print("Hello,", name["fname"], name["mname"], name["lname"])

# ab dekh
insta(mname="Sanyam",lname="soni",fname="MR.")

# ek return bhi hota h jisse function k output ki value kisi variable me save kr skte h hm
def bhoomi(a):
    return("The percentage is: ", a/100) # agr m ek se jyada return lga dunga to print bs phle vala hoga baki sare ignore mar diye jayenge
    return 7 # lekin agr ekla yhi hota to value 7 hi aati mtlb jo return k ander likhenge vhi print hoga 
# return ka mtlb vapas chale jao is value ko leke
c= bhoomi(2)
print(c)
# yanha pr ye jo is function ki value aayegi to vo c variable me store ho jaygi 
# jise me aage or bhi convenient tarike se use kr skte h