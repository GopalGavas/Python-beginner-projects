name = input("Enter your name:")


playing = input("Are your ready for the adventure..?\n")


if(playing.lower() != "yes"):
    quit()

print(f"Welcome {name} to this adventure!!..Let's begin")


answer = input("You are walking dirt road which came to an end. You have two choices, you can go right or left.which way will you go..?\n").lower()

if answer == "left":
    answer = input("You have come to a river,You can walk around it or swim across what will you do..? Type walk to walk around or swim to swim across\n").lower()

    if answer == "walk":
        print("You walked around a river for a mile and ran out of time, you lost the game, Better luck next time")
    elif answer == "swim":
        print("You swam and were eaten by a alligator :( , You lose")
    else:
        print("Not a valid option. You lose :(")

elif answer == "right":
    answer = input("You came across a jungle, do you want ro cross it quickly or you want to explore..?type cross to cross it quickly or type explore to explore\n").lower()

    if answer == "cross":
        answer = input("You quickly crossed the jungle and meetup with a stranger, do you want to talk to him..?type(yes/no)\n").lower()

        if answer == "yes":
            print("You talk to a stranger and he gives you his treasure, You Won!!! Congratulations!!")
        elif answer == "no":
            print("You don't talk to stranger and he his offended you don't find the treasure you lose :(")
        else:
             print("Not a valid option. You lose :(")

    elif answer == "explore":
        print("You explore the jungle and are eaten by a lion.. :( ,you lose")
        
    else:
        print("Not a valid option. You lose :(")

else:
    print("Not a valid option. You lose :(")


print(f"Thank you for playing {name}")