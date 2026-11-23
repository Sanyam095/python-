tup = (1,2,76,342,32,"Green",True)
# tuple ko hm change nhi kr skte 
# or tuple me kisi bhi type ka data dal skte h 
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
# print(tup[342]) # ye glt ho jayga
# ha or agr hme ek element ka tuple bnana h to hm comma jrur lgayenge nhi to python interpritor bawla ho jata h 
tupl = (1,)
print(type(tupl))
# ye tuple mana jayga
tu = (1)
print(type(tu))
# or ye integer mana jayga
if 342 in tup:
    print("Yes 342 is present in this tuple")

### list ki hi traha same to same slicing or jumping isme bhi hoti h 
# lekin slicing k bad ek nya tuple milta h 
# mtlb purane vala change hi nhi ho skta
tup2 = tup[1:4]
print(tup2)


# tuple and strings are immutable 
# lists are mutable
