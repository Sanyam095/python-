try:
    l = [1, 2, 3]
    i = int(input("Enter the index of the list: "))
    print(l[i])
except:
    print("An error occurred")
finally:
    print("This will always be executed")
print("This will also be executed")
# log khte h ki finally ko kyu bnaya jb hm normally bhi print kr skte h 
# iska answer hme jb milta h tb hm function ko use krte h
def func1():
    try:
        l1 =[2,5,7,3]
        i = int(input("Enter the index: "))
        print(l1[i])
        return "I love my life"
    except:
            print("Some error occurred")
            return "Fuck you life"
    finally:
        print("Meaning of life") # lekin dhayan rkhna ki ye line return vali line se ple print hogi
x = func1()
print(x)
# by the way ye question interviews me aata h 
# or bhot popular h
# tujhse bhi bhadwe