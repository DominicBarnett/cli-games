from random import randint

name = input("Greetings, What is your name? > ")
print("Greetings" , name)

roles = ["Bear", "Ninja", "Cowboy"]

computer = roles[randint(0,2)]
player = False
while player == False:
    player = input("Bear, Ninja, or Cowboy? > ")


    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
        else: #computer cowboy player ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!",player , "shoots", computer)
        else: #computer bear player ninja
            print("You lose!", player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
        else: #computer ninja player bear
            print("You win!", player, "eats", computer)
    play_again = input("Would you like to play again? (yes/no) >")
    if play_again =='yes':
        player = False
    computer = roles[randint(0,2)]
else:
    print("Have a good day")