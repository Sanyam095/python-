import time
def usingWhile():
    i = 0
    while (i<50000):
        print(i)
        i = i + 1

def usingFor():
    for i in range(50000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init

init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

# ek time.sleep bhi hota hai
print(4)
time.sleep(3)
print("This is printed after 3 seconds")
