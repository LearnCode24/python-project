from words import words
import random 
import os 
# word_list=["apple","banana","mango","orange"]


hangman_art={0:(" ",
                " ",
                " "),
             1:("O",
                " ",
                " "),
             2:("O",
                "|",
                " "),
             3:(" O",
                "/|\\",
                ""),
             4:(" O",
                "/|\\",
                "/ \\")}

def display_hangman(wrong_guess):
    print("---HANGMAN---")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("-------------")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

    

def prefill(answer,hint,guessed_letter):
    unique_letter=list(set(answer))
    if len(answer)<=6:
        reveal_count=2
    else:
        reveal_count=3

    reveal_count=min(reveal_count,len(unique_letter))
    letter_to_reveal=random.sample(unique_letter,reveal_count)
    for letter in  letter_to_reveal:
        guessed_letter.add(letter)
        for i in range(len(answer)):
            if answer[i]==letter:
                hint[i]=letter

def main():
    answer=random.choice(words())
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letter=set()
    prefill(answer,hint , guessed_letter)
    is_running=True
    while is_running:
    
        display_hangman(wrong_guess)
        display_hint(hint)
        guess=input("Enter a letter:").lower()
        if len(guess)!=1 or  not guess.isalpha():
            print("Invalid Input!")
            continue
        if guess in guessed_letter:
            print(f"{guess} is already guessed!")
            continue
        else:
            guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
               if answer[i]==guess:
                   hint[i]=guess
        else:
            wrong_guess+=1

        if "_"  not in hint:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("YOU WIN!")
            is_running=False
        elif wrong_guess==4:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("YOU LOSE!")
            is_running=False
    

if __name__=="__main__":
    main()