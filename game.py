import random

def play_game():
    lucky_num = random.randint(1,50)

    #user num input
    while True:
        user_num = int(input("guess the lucky num: "))

        if user_num == lucky_num:
            print("You won the Game!")
            break
        elif user_num < lucky_num:
            print("num is to low")
        else:
            print("num is to high")

    print("thank for play the game.")

play_game()