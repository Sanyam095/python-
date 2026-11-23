def my_generator():
    for i in range(500000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# isse hota kya hai ki ye pure 500000 numbers ko ek sath load nhi krge agr hm puchenge to load krega 
# isse processing speed fast ho jaaygi or memory ka usage km hoga
# jisse ki kam krte time to game bhi khel skta hai apni 16gb ddr4 me......
