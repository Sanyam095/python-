# sets kyu bnay jate h? 
# taki hm ek aaisa data type rkh ske jiske ander repeated entries na ho 
s = {2,4,2,6}
print(s)
# lekin ye ek unordered collection rkhta h 
# mtlb ese order se koi lena dena nhi h 
# isme alg alg data types bhi dal skte h 
info = {"Carla",19,False,5.9,19}
print(info)
# empty set bnane ka alg se method h 
harry = set() # aaise hi krna pdega 
# harry = {} # ye krunga to glt ho jayga
print(type(harry))

for value in info:
    print(value)
    