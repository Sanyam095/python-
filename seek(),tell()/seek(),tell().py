with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file 
    f.seek(10) # iska mtlb m phli 10 bytes ko skip kr k 11th byte pr ja rha hu

    #agr mujhe pta krna h ki meine kha tk seek() kiya hua h to m f.tell() lga dunga
    print(f.tell()) 

    # Read the next 5 bytes from the current position
    data = f.read(5)
    print(data)

# ek turncate bhi hota h 
with open ('sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5) # ynha meine compiler bhaisahab ko keh diya ki meri file ka size 5 bytes ka hona chaiye

with open('sample.txt', 'r') as f:
    print(f.read())  
    # Output: Hello aayega kyouki file ka size 5 bytes ka ho gya h