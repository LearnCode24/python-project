import random
import time
#Random Number guessing game program 
start=time.time()
highest=100
lowest=1
secret_number=random.randint(lowest,highest)
guesses=0
print("Python Random Guessing Number Game")
print(f"Guess Number between {lowest} and {highest}.")
while True:
    guess=input("Enter a number:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess>secret_number:
            print("Too high! Try again.")
        elif guess<secret_number:
            print("Too low! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            break

        
    else:
        print("Invalid Number!")
        print(f"Please guess Number between {lowest} and {highest}.")

end=time.time()
time_taken=end-start
print(f"The number guesses and time is {guesses} and {round(time_taken)} second.")
