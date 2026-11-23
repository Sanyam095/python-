# hmne while loop python me esiliye dale h taki programmers ka  time bach ske
i = 0         # phle me ek variable bna lunga or uski value de dunga 
while (i<3):  # phir m while loop open krunga or  condition de dunga
    print(i)  # phir ye condition ko check krega or print hota rhega jbtk ki i ki value 3 nhi ho jati
    i = i + 1 # kyouki m i ki value 1 se bda rha hu jo ki hr eytration k sath bdhti jaygi
print("Done with 1st loop")


# ulta while loop yani decrementing while loop bhi bna skta hu m
count = 5
while (count>0):
    print(count)
    count = count-1  # agr meine count = count+1 kr diya hota to ye ek infinite loop bn jayga
print("Done with 2nd loop")


# hm while loop k sath else ka estemal bhi kr skte h
c =8
while (c>2):
    print(c)
    c=c-1
else:
    print("I am inside else")
# jb while loop ki condition false ho jaygi to interpreter while loop se bhar aa jayga or else statement ko print kr dega


# m user se input bhi le skta hu 
i = int(input("Enter the number: "))
while (i <=78):
    i = int(input("Enter the number: "))
    print(i)
    # ye ek do while loop bn gya python me bhai dhayan rakhna kyouki ye aata h interviews me
    # do while loop me ek speciality hoti h ki vo km se km ek bar to execute hota hi hota h
    # ek or bhi acha or convenient trika hota h do while loop ko python me emulate krne ka
    # vo likhna h yanha agli ved dekh kr