
f = open("myfile.txt", "r")  # isme r ka mtlb read, w ka mtlb write, a ka mtlb append, x ka mtlb create, rt ka mtlb read text and rb ka mtlb read binary hota hai.
# binary file exe img pdf ved etc hoti h
text = f.read()
print(text)
f.close()

# dekh ab meine r likha second atribute me to mujhe f.read likhna pdega agr m w likhta to m f.write likhta aur agr a likhta to m f.append likhta.

# agr meine write mode me kisi aaisi file ko khol diya jo exist nhi krti h to python us file ko create kar dega aur usme likhne ke liye ready ho jaega. Lekin agar read mode me kholne ki koshish karunga to error aayega kyunki file exist nahi karti.

                                                # WRITING A FILE
f = open("myfile2.txt", "w")  # isme w ka mtlb write hota hai
f.write("Hello, World!")
f.close()

                                                # APPENDING A FILE
f = open("myfile2.txt", "a")  # isme a ka mtlb append hota hai
f.write("\nThis is an appended line.")
f.close()


# agr mujhe bar bar close krne ki bhadak nhi leni to with ka use krunga
with open("myfile.txt", "a") as f:
    f.write("Hey i am inside with")