# f = open("myfile.txt", "r")

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break

f = open("myfile2.txt", "r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Mark of student {i} in maths is {m1*2}")
    print(f"Mark of student {i} in science is {m2*2}")
    print(f"Mark of student {i} in english is {m3*2}")
    print(line)



                                                    # Writeline Method
f = open("myfile3.txt", "w")
lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]
f.writelines(lines)
f.close()

# agr bhot bdi files ho to:
f = open("myfile4.txt", "w")
lines = ["line1", "line2", "line3"]
for line in lines:
    f.write(line + "\n")
    f.close()