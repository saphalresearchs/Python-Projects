import random
def play():
    print("Welcome to Our Number Guessing Game. \nYou can set lower bound and upper bound to guess a number in " \
    "that range. You will get 6 chances to guess.")
    try:
        low = int(input("Enter lower bound"))
        high = int(input("Enter higher bound"))
        f = random.randint(low,high)
    except ValueError:
        print("Please Enter Valid numbers!")
        return
    
    gc = 0
    ch = 6

    for i in range(1,ch+1):
        try:
            t = int(input(f"Attempt ({i}, {ch+1-i}). Enter your guess number.\n"))
        except ValueError:
            print("Invalid input. Counting as a missed turn!")
            continue
        if t==f:
            print("Correct guess!")
            break
        elif t>f:
            print("Your guess is high\n")
        else:
            print("Your guess is low\n")   
    print(f"Game Over! The correct number was {f}")

def play_again():
    while True:
        a = input("Do you want to play this game(y/n)?").lower().strip()
        if a == "y":
            return True
        if a == "n":
            return False
        print("Please enter ")
    
if __name__ == "__main__":
    playing=True
    while playing:
        play()
        playing = play_again()

    
# a= str(input("Do you want to play this game? Type Y for Yes\n"))
# print(a)
# if str.upper(a) == "Y":
#     again()


