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
            print(f"Your guess is correct. {i} Attempt taken.")
            return
        elif target > guess:
            print("Your Guess is low")
        else:
            print("Your guess is High")
    print(f"Game Over! The Correct number was {target}")

def play_again():
    while True:
        choice = input("Do you want to play again(y/n)?").lower().strip()
        if choice == "y":
            return True
        if choice == "n":
            return False
        print("Enter y for yes and n for no")

if __name__== "__main__":
    playing=True
    while playing:
        play()
        playing = play_again()

    print("Thanks for Playing. Goodbye!!")

