import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter the time in hours: "))

if (hour>=0 and hour<12):
    print("Good Morning Sir")
elif (hour>= 12 and hour<16):
    print("Good Afternoon Sir")
elif (hour>=16 and hour<0):
    print("Good Night Sir")