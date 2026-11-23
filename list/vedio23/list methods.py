l = [1,2,4,6]
print(l)
# ye thi ek list bilkul seedhi sadhi sarif si
# ab agr m chahata hu ki es list k last me ek or element add ho jay to m append ka use krunga
print(l.index(1)) # agr mujhe list me kisi element ka index chaiye ho to aaise krunga
l.append(7)
print(l) # agr m yanha print(l) nhi likhta to l.append(7) command print nhi hoti # mtlb hme koi bhi change krke print krna pdta h 

li =[2,6,0,23,4,24,64,9,5]
# ab m chahata hu ki meri ye list sortout ho jay 
li.sort() # esse meri list sort ho jaygi mtlb accending order me lg jaygi
print(li)
li.sort(reverse=True) # ye decending order me kr dega
print(li)
li.reverse() # ye hmari original list ko reverse kr dega
print(li) # lekin is point pr hmari list change ho chuki h to output alg aayega
# in sbhi ka bhi same h 
lst= [9,4,8,32,4,25,1,6,1,4,8,4,0,1,4,6]
print(lst.count(1)) 
print(lst.count(4)) # ya to bad me print statement lga de ya to tu sath ki sath me bhi lga skta h

# agr m ek nyi list bna du or us list ko li k brabr kr du 
# or agr m us nyi list ko change krunga to meri original li list bhi change ho jaygi
# agr mujhe in cheejo se bachna h to copy statement ka use krna hoga
# m = lst
# m[0] = 0
# print(lst)
# inse confusion create ho skta h 
m = lst.copy()
m[0] = 0
print(lst)
# ab list same hi h vrna change ho jati agr m copy nhi krta to

## agr m chahu to list me khi bhi kuch bhi inset kr skta hu 
lst.insert(1,100) # iska mtlb h ki m lst list me 2nd no pr 100 nam k ek element ko insert krna chahata hu jo ki ek number h 
print(lst)

# ek or bhot imp cheej h
# jb hme kisi list ko uthake dusri list k end me ptkna ho to hm extend ka use krte h 
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b) # iska mtlb mujhe a list k end me b list ko ptkna h 
print(a)
# lekin iska ek ghata h 
# a.extend krne se to mera a change ho jayga
# lekin agr m chahata hu ki mera a change na ho to bhi ek rasta h 
a1=[1,2,3,4,5]
b1=[6,7,8,9,10]
k = a1 + b1
print(k)
# ab a1 aur b1 change nhi honge