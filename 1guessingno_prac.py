import random
def play():
    print("Welcome to Our game:")
    try:
        low = int(input("Enter lower bound"))
        high = int(input("Enter higher bound"))
    except ValueError:
        return
    target = random.randint(low, high)
    chances = 6
    for i in range(1, chances+1):
        try:
            guess = int(input(f"Attempt {i,chances}\t Please enter your guess."))
        except ValueError:
            print("Format error. Counting as a incorrect guess ...")
            continue
        if target == guess:
            print("Your guess is correct. Attempt")