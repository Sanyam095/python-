names="Sanyam,Harry"
print(names[0:6]) # iska mtlb h ki m 0 se 6-1 tk k char ko print krna chahata hu 
# or print bhi sanyam hi hoga 
# programming krte time ginti hmesha 0 se start krni h 

# m kisi bhi string ki lengt len function se find kr skta hu
print(len(names))
fruit ="mango"
print(len(fruit))
print(fruit[:4])
# bhai python smajhdar h vo starting me zero khud lga lega
print(fruit[1:]) 
#ye 1 se start hoga aur end tk jayega
print(fruit[:])
# ye pura string print krega
print( fruit[0:-3]) # ye hm dekh rhe h 
# print( fruit[0:len(fruit)-3]) ye python dekh rha h
# mtlb vo 5 me se 3 ko automatically minus krke output de dega
print(fruit[-3:-1]) 
# phle python nisko len(fruit)-3 krdega jo ki 5-3=2 hoga
# fir python agle vale ko len(fruit)-1 krdega jo ki 5-1=4 hoga
# to iska mtlb print(fruit[-3:-1]) ho jayga


#quick quiz
nm ="harry"
# print(nm[-4:-3])
# iska mtlb print(nm[1:2]) hoga
# iska answer a hoga