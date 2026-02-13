import random
print("Welcome to Our Number Guessing Game. \nYou can set lower bound and upper bound to guess a number in " \
"that range. You will get 6 chances to guess.")

low = int(input("Enter lower bound"))
high = int(input("Enter higher bound"))
f = random.randint(low,high)

gc = 0
ch = 6

while gc<ch:
    gc+=1
    t = int(input(f"Enter your guess number. You have {ch-gc+1} chances availabe\n"))

    if t==f:
        print("Correct guess!")
        break
    elif gc>=ch and t!=f:
        print(f"Chances over. {f} was the number.")
    elif t>f:
        print("Your guess is high\n")
    else:
        print("Your guess is low\n")   
    
