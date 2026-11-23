def welcome():
    print("Hey there! Welcome to the program.")

print(__name__)
if __name__ == "__main__":
    welcome()
    # iska mtlb agr __name__ ki value __main__ h mtlb ki programme ko ynhi se run kiya ja rha h mtlb welcome() ko run krna h. 
    # or agr __name__ ki value __main__ k alava kuch or h mtlb is file ko ynha se run nhi kiya ja rha h mtlb welcome() run nhi krna h. 
    # kisi bhi local file me uska nam __main__ hi manke chal chutiye. 