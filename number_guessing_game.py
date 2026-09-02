import random
import time
#Random Number guessing game program 
start=time.time()
secret_number=random.randint(1,100)
count=0
while True:
    number=int(input("Enter a secret number:"))
    count+=1
    if number>secret_number:
        print("Too high!")
    elif number<secret_number:
        print("Too low!")
    else:
        print(f"You have guessed right! The Correct Number is {secret_number}")
        break
    
end=time.time()
print(f"The no  of guesses and time you took is {count} and {end-start:.1f} seconds respectively.")
