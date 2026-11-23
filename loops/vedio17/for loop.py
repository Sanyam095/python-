name = ("Abhishek")    # ab name ek string h to string k hr ek chacracter ko x ek ek krke apni value bnata rhega 
for x in name:         # or fir print bhi ho jayga
    print(x)              # ye string ka example tha
    if (x=="b"):
        print("This is something special!")          

# for x in name:
#     if (x=="b"):
#         print(x)
#         print("This is something special!")
#     else:
#         print(x)

colours = ["Red", "Green", "Blue", "Yellow"]
for colour in colours:
    print(colour)  # ye list ka example h
    # or mujhe agr red green etc k ek ek word bhi chaiye to m vo bhi kr skta hu
    for i in colour:
        print(i)
# ek range ka concept bhi hota h
for a in range(5):  
    print(a)
# ye 0 se 5-1 tk print krega
# hm isko control bhi krs skte h
for z in range(1,5):
    print(z)
for n in range (0,2000):
    print(n+1)
for n in range (1,20,3):
    print(n)