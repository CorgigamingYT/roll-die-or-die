import random
import time


def p1(text):
    print(text)


def p2(text, score):
    print(text)
    print(int(score))


def p3(text, score, score2):
    print(text)
    print(int(score))
    print(int(score2))


def playround():
    rounds = 1
    if rounds == '1':
        rounds = rounds + 1
    dice1roll1 = random.randint(1, 6)
    dice2roll1 = random.randint(1, 6)
    even = [2, 4, 6, 8, 10, 12]
    odd = [1, 3, 5, 7, 9, 11]
    print("ROUND ", rounds)
    time.sleep(1)
    p3("Your first numbers are", dice1roll1, dice2roll1)
    points = dice1roll1 + dice2roll1
    time.sleep(1)
    score1 = sum = float(dice1roll1) + float(dice2roll1)
    if score1 in even:
        p1("+10 points")
        points = points + 10
    else:
        p1("-5 points")
        points = points - 5
    if points <= 0:
        points = + 1
        p1("Have a point. On us.")
    time.sleep(1)
    print("Your score after round ", rounds,  "is:", points)
    nr = input("To play next round, press y ").lower()
    if nr == 'y':
        rounds = rounds + 1
        playround()
    playround()


user = input("Please enter a username: ")
if user == "yeet":
    password = input("Please enter a password: ")
    if password == "yoot":
        p1("Hello " + user)
        time.sleep(1)
        p1("Do you want to start? ")
        time.sleep(1)
        print("""
1. One Player
2. Two Player
3. Exit
""")
        yn = input("Please choose: ")
        if yn == "1":
            playround()
