import random 

def main():
    options=("rock","paper","secissor")
    score=0
    print("----------------GAME STARTS---------------- ")

    playing=True
    while playing:
        player_choice=None
        computer_choice=random.choice(options)

        while player_choice not in options:
            player_choice=input("Enter  your choice (rock ,paper,secissor):")
            print(f"Your choice :{player_choice} ")
            print(f"Computer choice:{computer_choice}")

        if computer_choice==player_choice:
            print("It's a tie!")
        elif player_choice=="paper" and computer_choice=="rock":
            print("You win!")
            score+=1
        elif player_choice=="secissor" and computer_choice=="paper":
            print("You win!")
            score+=1
        elif player_choice=="rock" and computer_choice=="secissor":
            print("You win!")
            score+=1
        else:
            print("You lose!")

        play_again=input("Do you wanna play (yes/no):").lower()
        while not(play_again=="yes" or play_again=="no"):
            play_again=input("Please enter yes/no:")
        if play_again=="yes":
            pass 
        else:
            playing=False

        
    print("Thanks for playing !")
    print(f"Your score is {score}")
    print("----------------GAME OVER---------------- ")

if __name__=="__main__":
    main()
