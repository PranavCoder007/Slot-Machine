import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROW = 3
COLUMN = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_line.append(line + 1)

    return winnings, winning_line

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:] #makes copy of the all_symbol. So if Current_symbol changes there will be no change in the all_symbol
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What is that you want to deposit? Rs.")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Pleases enter the amount greater than zero")

        else:
            print("Please enter integer")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the no of lines to bet on (1-"+str(MAX_LINES)+")")

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Pleases enter a valid no of lines")

        else:
            print("Please enter integer")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? Rs. ")

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Pleases enter the bet between Rs.{MIN_BET} - Rs.{MAX_BET}")

        else:
            print("Please enter integer")

    return amount

def spins(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to place such bet. Your current balance is Rs.{balance}")
        else:
            break

    print(f"You have bet Rs.{bet} on {lines} lines. Total bet is: Rs.{total_bet}")

    slots = get_slot_machine_spin(ROW, COLUMN, symbol_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print(f"You won Rs.{winnings}.")

    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()

    while True:
        print(f"Your current balance is Rs.{balance}")

        spin = input("Press enter to play (or q to quit)")

        if spin == "q":
            break

        balance += spins(balance)

    print(f"Your final balance after the bets is Rs.{balance}")


main()