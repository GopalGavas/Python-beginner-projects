import random

user_wins = 0
computer_wins = 0 

options = ["rock", "paper" , "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit.\n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #0=rock , 1=paper, 2=scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "scissors" and computer_pick == "paper":
        print("You won!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("you won!!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("Its a draw")
        # user_wins += 1
        # computer_wins += 1

    else:
        print("You lost")
        computer_wins += 1


print(f"You won {user_wins} times")
print(f"The computer won {computer_wins} times")
print("Goodbye!!")
