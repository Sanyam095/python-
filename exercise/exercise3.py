                                            ### Kon Bnega Crorepati ###
                       # Question: Create a programme of displaying questions to the user like KBC
                       # Use list data type to store the questions and their answers
                       # Display the final amount the person is taking home after playing the game


que1 = "Bharat ki rajdhani kya hai?" # delhi  # 1000
que2 = "Computer ka dimaag kise kaha jata hai?" # cpu  2000
que3 = "\"Jai Jawan Jai Kisan\" ka naara kisne diya tha?" # lal bhadur shastri  #5000
que4 = "Minecraft me Creeper kis rang ka hota hai?" # hara #10000
que5 = "NDA ka full form kya hai?" #National Defence Academy #20000
que6 = "Kis grah ko \"Red Planet\" kaha jata hai?" # Mars #40000
que7 = "Python kis prakar ki language hai?" # Programming Language #80000
que8 = "Bharat ka rashtriya pashu kaun sa hai?" #Bagh #160000
que9 = "Kis company ne ChatGPT banaya hai?" #OpenAI # 320000
que10 = "World Wide Web ka avishkar kisne kiya tha?" # Tim Berners-Lee #640000
l1 =[que1,que2,que3,que4,que5,que6,que7,que8,que9,que10]
# l2 =["Delhi","CPU","Lal Bhadur Shastri","National Defence Academy","Mars","Programming Language","Bagh","OpenAI","Tim Berners-Lee"]
print("\t \t \t \t \t \t  KBC ka phla swal aapki screen pr")
print("\t \t \t \t \t \t \t \t 1000Rs k liye")
print(l1[0])
print("""A. Mumbai
B. Kolkata
C. New Delhi
D. Chennai""")
a1 = input("Enter the correct option here: ")
if(a1=="C"):
    print("CONGRATS!\n \t\tYOU WON 1000 RS")
    print("KBC ka dusra swal aapki screen pr")
    print("2000Rs k liye\n")
    print(l1[1])
    print("""A. RAM
B. CPU
C. Hard Disk
D. Monitor""")
    a2 = input("Enter the correct option here: ")
    if (a2=="B"):
        print("CONGRATS!\n \t\tYOU WON 2000 RS\n Now you have 3000Rs")
        print("KBC ka tesra swal aapki screen pr")
        print("5000Rs k liye\n")
        print(l1[2])
        print("""A. Jawaharlal Nehru
B. Lal Bahadur Shastri
C. Indira Gandhi
D. Mahatma Gandhi""")
        a3 =(input("Enter the correct option here: "))
        if (a3=="B"):
            print("CONGRATS!\n \t\tYOU WON 5000 RS\n Now you have 8000Rs")
            print("KBC ka chautha swal aapki screen pr")
            print("10000Rs k liye\n")
            print(l1[3])
            print("""A. Laal
B. Neela
C. Hara
D. Peela""")
            a4 =input("Enter the correct option here: ")
            if (a4=="C"):
                print("CONGRATS!\n \t\tYOU WON 10000 RS\n Now you have 18000Rs")
                print("KBC ka panchva swal aapki screen pr")
                print("20000Rs k liye\n")
                print(l1[4])
                print("""A. National Defence Academy
B. National Development Academy
C. New Defence Association
D. National Duty Academy""")
                a5 = input("Enter the correct option here: ")
                if (a5=="A"):
                    print("CONGRATS!\n \t\tYOU WON 20000 RS\n Now you have 38000Rs")
                    print("KBC ka chatha swal aapki screen pr")
                    print("40000Rs k liye\n")
                    print(l1[5])
                    print("""A. Venus
B. Jupiter
C. Mars
D. Saturn""")
                    a6 = input("Enter the correct option here: ")
                    if (a6=="C"):
                        print("CONGRATS!\n \t\tYOU WON 40000 RS\n Now you have 78000Rs")
                        print("KBC ka satva swal aapki screen pr")
                        print("80000Rs k liye\n")
                        print(l1[6])
                        print("""A. Programming Language
B. Operating System
C. Browser
D. Database""")
                        a7 =input("Enter the correct option here: ")
                        if (a7=="A"):
                              print("CONGRATS!\n \t\tYOU WON 80000 RS\n Now you have 158000Rs")
                              print("KBC ka satva swal aapki screen pr")
                              print("160000Rs k liye\n")
                              print(l1[7])
                              print("""A. Sher
B. Bagh
C. Hathi
D. Mor""")
                              a8 =input("Enter the correct option here: ")
                              if (a8=="B"):
                                print("CONGRATS!\n \t\tYOU WON 160000 RS\n Now you have 318000Rs")
                                print("KBC ka satva swal aapki screen pr")
                                print("320000Rs k liye\n")
                                print(l1[8])
                                print("""A. Google
B. Microsoft
C. OpenAI
D. Meta""")
                                a9 =input("Enter the correct option here: ")
                                if (a9=="C"):
                                    print("CONGRATS!\n \t\tYOU WON 320000 RS\n Now you have 638000Rs")
                                    print("KBC ka satva swal aapki screen pr")
                                    print("640000Rs k liye\n")
                                    print(l1[9])
                                    print("""A. Bill Gates
B. Steve Jobs
C. Tim Berners-Lee
D. Mark Zuckerberg""")
                                    a10 =input("Enter the correct option here: ")
                                    if (a10=="C"):
                                        print("CONGRATS!","\nYou won the entire game")
                                        print("CONGRATS!\n \t\tYOU WON 640000 RS\n Now you have 1278000Rs")
                                    else:
                                         print("Your answer is incorrect")
                                         print("You have to go with your 638000Rs")
                        else:
                                print("Your answer is incorrect")
                                print("You have to go with your 318000Rs")
                    else:
                              print("Your answer is incorrect")
                              print("You have to go with your 158000Rs")
                else:
                        print("Your answer is incorrect")
                        print("You have to go with your 38000Rs")
            else:
                     print("Your answer is incorrect")
                     print("You have to go with your 1800Rs")
        else:
            print("Your answer is incorrect")
            print("You have to go with your 3000Rs")
    else:
        print("Your answer is incorrect")
        print("You have to go with your 1000Rs")
else:
    print("You loose")
print("The game is over now")