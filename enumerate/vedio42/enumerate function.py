# Aam jindgi
marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Harry, awesome!")
#     index +=1

for index,mark in enumerate(marks,start=1):# yanha m start = 1 likh kr ye bhi bta skta hu ki index start kha se krna h
    print(mark)
    if(index == 3):
        print("Harry, awesome!")
# yanha enumerate aapko value k sath sath index bhi de deta h 
# index, mark hi likhna h mark,index likh diya to glt ho jayga