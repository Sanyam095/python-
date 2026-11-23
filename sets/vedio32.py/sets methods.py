s1 ={1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2))
# Bhai common! tujhe pta h ki union kya hota h 
# lekin ye set1 ya set2 me koi change nhi krta 
# agr change krna h to ye use kro
s1.update(s2)
# iska mtlb ye update kr dega
print(s1,s2)
# or intersection ka bhi pta h tujhe
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
# common you know all about intersection

## recall symmetric difference of sets = (A union B) - (A intersection B)
cities4 = cities.symmetric_difference(cities2)
print(cities4)
# update method se set update ho jayga
# ek differencce method bhi hota h 
cities5 = cities.difference(cities2)
print(cities5) 
# iska mtlb ye cities me se cities2 ke elements ko remove kr dega

# is disjoint bhi hota h 
# disjont sets vo hote h jinka intrsection fi hota h 
c1 = {1,2,3}
c2 = {4,5,6}
print(c1.isdisjoint(c2))
# ab inme koi common element nhi h to ye true dega
# agr hota to ye false deta

# ek issuperset bhi hota h
a1 ={"Tokyo", "Madrid", "Berlin", "Delhi"}
a2 = {"Wano", "Kabul"}
print(a1.issuperset(a2))
# issuperset ka mtlb h ki a1 me a2 ke sare elements hone chahiye
# is case me ye false dega
# ha or ye output boolen me hi deta h

#issubset bhi hota h
a3 = {"Tokyo", "Madrid"}
print(a3.issubset(a1))
# iska answer true h kyuki a3 ke sare elements a1 me h
city = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city.add("Wano")
print(city)
# add method se set me element add kr skte h
# agr do sets ko jodna h to update krlo
city.update({"Kabul", "Seoul"})
print(city)
# remove method se element remove kr skte h
city.remove("Delhi")
print(city)
# discard method bhi hota h remove ki tarah hi h lekin ye error nhi deta jb hm koi aaisa element discard kr de jo ki set me h hi nhi 
# lekin remove error dega
city.discard("Kabul")
print(city)
# ek pop method bhi hota h jo ki random element ko remove krta h set se

#ek del bhi hota h jo ki set ko delete kr deta h
del city
# print(city)
# ye error dega kyuki city set delete ho chuka h

# agr mujhe pura set delete nhi krna bs items clear krna h to clear method use kr skte h
s = {1,2,3,4,5}
s.clear()
print(s)
# hm ye bhi dekh skte h ki set me koi element h ya nhi
s = {1,2,3,4,5}
if 3 in s:
    print("3 is present in the set")
else:
    print("3 is not present in the set")