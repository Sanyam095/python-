print("THE LEGENDARY GAME ")
print("Stone Paper Scissors\n\n")
import random
print("(for choose stone press 1, for choose paper press 2, for choose scissors press 3)\n\n")
user = int(input("Enter your choice: "))
comp = random.randint(1,3)

print(f"Your choice: {user}")
print(f"Computer's choice: {comp}")
if user == 1:
    if comp == 1:
        print("Its a draw!")
    if comp == 2:
        print("You loose!")
    if comp == 3:
        print("You win!")
if user == 2:
    if comp == 1:
        print("You win!")
    if comp == 2:
        print("Its a draw!")
    if comp == 3:
        print("You loose!")
if user == 3:
    if comp == 1:
        print("You loose!")
    if comp == 2:
        print("You win!")
    if comp == 3:
        print("Its a draw!")

a = input("Do you want to play again?: ")


if a:
    import exercise5