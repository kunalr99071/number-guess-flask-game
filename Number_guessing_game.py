import random

def greet(name):
    print(f"Hello {name}")
    rules()

def rules():
    print("================= Rules =================")
    print("1. Select number between 1 to 100.")
    print("2. You only get 5 chances.")
    print("3. Press 0 to exit the game.")
    generate_random_number()

def generate_random_number():
    num = random.randint(1,100)
    game(num)

def game(num):
    print("Let's Start The Game")

    count = 1

    while count <= 5:
        guess = int(input("Guess Number : "))

        if guess == 0:
            print("Game Exited")
            break

        if guess < 1 or guess > 100:
            print("Please enter number between 1 to 100.")
            continue

        if guess < num:
            print("Small")
        elif guess > num:
            print("Large")
        else:
            print("******* YOU WON *******")
            return

        count += 1

    if count > 5:
        print("*** BETTER LUCK NEXT TIME ***")
        print("Correct number was:", num)

greet("Kunal")