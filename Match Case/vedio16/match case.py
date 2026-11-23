x = int(input("Enter the value of x: "))
# dekh ab is x ko match krke dikhata hu
match x:
    case 0:
        print("x is Zero")
    case 1:
        print("x is one")
    case 2:
          print("x is two")
    case 3:
        print("x is three")
    case 4:
        print("x is four")
# ek default case bhi hota h "_" vala
    case _ if (x !=90):  # isme ek catch h ki agr ye condition phle met ho gyi to bs yhi chapegi 
        print(x," is not equals to 90") # or niche vale nhi chapenge
    case _ if (x !=80): 
              print(x," is not equal to 80") # iske sath bhi same seen h 
    case _:
          print(x) # iske sath bhi same seen h

# ek mje ki bat ki ye match vali commands hm bs python 3.10 or uske aage vale versions me hi chala skte h
# mtlb modern python developers only