import random
import time

SYMBOLS = ['🍒', '🍉', '🍋', '🔔', '⭐']

def get_win_chance(bet, max_bet=100):
    chance = 0.05 + (bet / max_bet) * 0.35
    return min(chance, 0.40)


def spin_row(bet):
    win_chance = get_win_chance(bet)
    if random.random() < win_chance:
        symbol = random.choice(SYMBOLS)
        return [symbol, symbol, symbol]
    else:
        while True:
            row = [random.choice(SYMBOLS) for i in range(3)]
            if not (row[0] == row[1] == row[2]):
                return row


def print_row(row):
    
    time.sleep(0.5)

    
    for i in range(8):
        flicker = [random.choice(SYMBOLS) for j in range(3)]
        print("| " + " | ".join(flicker) + " |", end="\r")
        time.sleep(0.1)

    
    revealed = ["?", "?", "?"]
    for position in range(3):
        for i in range(4):
            revealed[position] = random.choice(SYMBOLS)
            print("| " + " | ".join(revealed) + " |", end="\r")
            time.sleep(0.1)
        revealed[position] = row[position]
        print("| " + " | ".join(revealed) + " |", end="\r")
        time.sleep(0.3)
    final_text = "| " + " | ".join(row) + " |"
    border = "-" * (len(final_text) + len(row))
    print(border)
    print(final_text)
    print(border)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = int(input("Enter your balance: "))
    print("**************************************")
    while True:
        print(f"Your current balance Rs.{balance}.")
        bet = input("Enter your bet amount: ")
        print("**************************************")

        if not bet.isdigit():
            print("Please, enter a valid amount!")
            continue

        bet = int(bet)

        if bet < 0:
            print("Bet can't be negative, please re-enter!")
            continue

        if bet > balance:
            print("Insufficient fund!")
            continue

        balance -= bet
        row = spin_row(bet)
        print("Spinning....")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won Rs.{payout}.")
        else:
            print("**************************************")
            print("Sorry you lost this round!")
        balance += payout
        if balance==0:
            break

        play_again = input("Do you wanna play again (Y/N): ").upper()
        while play_again != "Y" and play_again != "N":
            print("Invalid choice! Please enter Y or N.")
            play_again = input("Do you wanna play again (Y/N): ").upper()

        if play_again == "Y":
            continue
        else:
            break

    print("**************************************")
    print(f"Game over! Your final balance is Rs.{balance}")
    print("**************************************")

if __name__=="__main__":
    main()