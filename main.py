import random
import time


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not is_even(num)


def die_roll():
    return random.randint(1, 6)


def playround(round, score):
    dice_roll1 = die_roll()
    dice_roll2 = die_roll()
    print("ROUND ", round)
    time.sleep(1)
    print("Your first numbers are " + str(dice_roll1) + " " + str(dice_roll2))
    time.sleep(1)
    score = score + dice_roll1 + dice_roll2
    if is_even(score):
        print("Your total after that round is even so have 10 points")
        score += 10
    else:
        print("Your total after that round is odd so we will take away 5 points. Haahaa.")
        score -= 5
    if dice_roll1 == dice_roll2:
        die_roll3 = die_roll()
        print("You had 2 of the same value adding on another random number:  ." + str(die_roll3))
        score = score + die_roll3
    if score <= 0:
        score = 1
        print("Your points went below zero, setting points back to 1.")
    time.sleep(1)
    print("Your score after round ", round,  "is:", score)
    nr = input("To play next round, press y ").lower()
    if nr == 'y':
        playround(round+1, score)
    playround(round+1, score)


user = input("Please enter a username: ")
if user == "connor":
    password = input("Please enter a password: ")
    if password == "austin":
        print("Hello " + user)
        time.sleep(1)
        print("Do you want to start? ")
        time.sleep(1)
        print("""
1. Play
2. Exit
""")
        yn = input("Please choose: ")
        if yn == "1":
            playround(1, 0)
