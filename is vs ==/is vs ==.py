a = 4 
b = "4"
print(a is b) # exact location of object in memory
print(a == b) # value 
# output: false   false

a = [1, 2, 43]
b = [1, 2, 43]
print(a is b) # exact location of object in memory
print(a == b) # value
# output: false   true

a = 3 
b = 3
print(a is b) # exact location of object in memory
print(a == b) # value
# output: true   true
# iska mtlb ye h ki agr aaisa object lega jo changable h to wo alag alag location pr store hoga or agr aaisa object lega jo unchangable h to wo same location pr store hoga

a = "sanyam"
b = "sanyam"
print(a is b) # exact location of object in memory
print(a == b) # value
# output: true   true

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b) # exact location of object in memory
print(a == b) # value
# output: true   true

a= None
b= None
print(a is b) # exact location of object in memory
print(a == b) # value
print(a is None) # exact location of object in memory
# output: true   true  true

# Agr is lgayega to same location honi chaiye
# Lekin agr == lgayega to value same honi chaiye (class bhi bhdk)