# f-strings ka aavishkar hi string formatting ko theek krne k liye hua tha 
# phle log string formatting kuch aaise krte the
letter = "Hey my name is {0} and I am from {1}" # m yanha 0 or 1 ko replace krke iski value ko change bhi kr skta hu
name = "Sanyam"
country ="India"
print(letter.format(name,country))
#########################################################################################################################################################################
# lekin ab log kuch aaise krte h python 3.6 k bad se
print(f"Hey my name is {name} and I am from {country}")
# m isme direct name or country likh skta hu 
# khamkha ki jhanjhat hi nhi

txt = "For only {price: .2f} dollars!"
print(txt.format(price=49.09999999))
# ab ye bs point k bad ki do hi digit print krega lekin round off krke

# agr man lo ki hme f string k ander curly bracket lgani h "{}"
print("We use f-strings like this: Hey my name is {{name}} and I am from {{India}}")
# simple