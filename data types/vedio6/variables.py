# variables hote kya h ?
# variables ek khali container ki teraha hote h jisme hm apna data store kr skte h 
# bilkul usi teharar jaise hm ghar pr dal cheeni namak aadi store krte h
# ye container memory yani ki ram me store hota h 
# Ha vahi 16 gb ram teri jais__
a = 14738
print(a)
print(" ")
b="Sanyam"
print(b)
# jruri nhi ki a b c hi variables ho hm kuch bhi likhe skte h
# jaise ki ram
ram = 16.0
print(ram)

# print("a+b") krunga to error aayega
# kyouki ek to integer h or ek string h to unka sum nhi ho skta
a1 = 10
print("a+a1") 
# bhai meine yha pr chot si mistake kr di h agr pta h kya ki h to tu intelligent hone lga h ladle 


# agr m dono int ko add krunga to errer nhi aayega
# agr mujhe kisi bhi variable ka type dekhna h to hm type() function ka use kr skte h
print("type of a is ", type(a))
print("type of b is ", type(b))
print("type of ram is ", type(ram))
# aacha m aaise bhi kr skta hu
B= True # boolen data bs true ya false ho skte h
print("type of B is ", type(B))
c= 3+4j # complex no ka to tujhe pta hi h yr
print("type of c is ", type(c))
# thoda se list k bare me bhi dekh le 
list1 = [1,2.0,"sanyam",True,3+4j]  # list mutable hote h yani ki hm list ke andar data ko change kr skte h
print("type of list1 is ", type(list1))
print("list1 = ", list1)
# hm list k ander different type k data store kr skte h
# yanha tk ki chahe vo list khud hi kyu na ho
list2 = [1,2.0,"sanyam",True,3+4j,[1,2,3]]
print("type of list2 is ", type(list2))
print("list2 = ", list2)
# ek tuple bhi hote h list ki teraha  bs unme hm data ko change nhi kr skte mtlb vo immutable hote h
tuple1 = (1,2.0,"sanyam",True,3+4j,[1,2,3])
print("type of tuple1 is ", type(tuple1))
print("tuple1 = ", tuple1)
dict1 = {"name":"sanyam","age":20,"is_student":True} # dict bhi ek data structure hote h jisme hm key value pair me data store krte h
print("type of dict1 is ", type(dict1))
print("dict1 = ", dict1)

#extra ka gyan
# python me sb kuch ek object h
#ye aage pta lgega ki kya mtlb h iska