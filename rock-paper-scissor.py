import random


def play():
    complist = ("rock","paper","scissor")
    num = random.randint(0,2)
    comp_choice = complist[num]
    user_choice = raw_input("Rock apper scissors?(r/p/s)").lower()
    print("Computer choice: ",comp_choice)
    if (user_choice == "r"):
        print("You choose rock")
        if (comp_choice == "paper"):
            print("You loose!")
        elif comp_choice == "scissor":
            print("You Win")
        else:
            print("Draw!")
    elif user_choice == "p":
        print("You choose paper")
        if comp_choice == "scissor":
            print("You loose")
        elif comp_choice == "rock":
            print("You win")
        else:
            print("Draw!")
            
    else:
        print("You choose scissor")
        if comp_choice == "rock":
            print("You loose")
        elif comp_choice == "paper":
            print("You win")
        else:
            print("Draw!")

while True:

    choose = raw_input("Do you want to continue?(y/n)").lower()
    if choose == "y":
        play()
    else:
        print("Thanks for playing")
        break    
        



