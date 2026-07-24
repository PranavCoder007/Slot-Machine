# 🎰 Python Slot Machine Game

A simple command-line **Slot Machine Game** built in Python. The game allows players to deposit money, place bets on multiple paylines, spin the slot machine, and win rewards based on matching symbols.

This project demonstrates the use of Python fundamentals such as functions, loops, dictionaries, lists, input validation, and randomization.

---

## 📌 Features

* 💰 Deposit an initial balance
* 🎯 Bet on **1 to 3 paylines**
* 💵 Choose a bet amount for each selected line
* 🎰 Randomly generated 3×3 slot machine
* 🏆 Win rewards when all symbols in a selected row match
* 📉 Balance updates after every spin
* ✅ Input validation for deposits, bets, and paylines

---

## 🛠️ Technologies Used

* Python 3
* `random` module

---

## 📂 Project Structure

```
slot-machine/
│
├── slot_machine.py    # Main game source code
└── README.md          # Project documentation
```

---

## 🎮 How the Game Works

### 1. Deposit Money

The player starts by depositing an amount into their account.

Example:

```
What is that you want to deposit? Rs.1000
```

---

### 2. Select Number of Lines

Players can bet on **1 to 3 horizontal lines**.

```
Enter the no of lines to bet on (1-3): 3
```

---

### 3. Enter Bet Amount

Choose how much to bet on each selected line.

```
What would you like to bet on each line? Rs.50
```

Total Bet:

```
3 lines × Rs.50 = Rs.150
```

---

### 4. Spin the Slot Machine

A random 3×3 slot machine is generated.

Example:

```
A | C | A
B | B | B
D | C | D
```

---

### 5. Winning Rules

A player wins if **all three symbols in a selected horizontal line are identical.**

Example:

```
B | B | B
```

Each symbol has a payout multiplier.

| Symbol | Multiplier |
| ------ | ---------: |
| A      |         5× |
| B      |         4× |
| C      |         3× |
| D      |         2× |

If the bet is Rs.50 and the winning row is:

```
B | B | B
```

Payout:

```
4 × 50 = Rs.200
```

---

## ⚙️ Symbol Distribution

Different symbols appear with different frequencies, making higher-value symbols rarer.

| Symbol | Count |
| ------ | ----: |
| A      |     2 |
| B      |     4 |
| C      |     6 |
| D      |     8 |

Because **A** appears the least, it offers the highest reward.

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/slot-machine.git
```

Move into the project directory:

```bash
cd slot-machine
```

Run the program:

```bash
python slot_machine.py
```

or

```bash
python3 slot_machine.py
```

---

## 📸 Sample Gameplay

```
What is that you want to deposit? Rs.1000

Your current balance is Rs.1000

Press enter to play

Enter the no of lines to bet on (1-3): 2

What would you like to bet on each line? Rs.50

You have bet Rs.50 on 2 lines.
Total bet is: Rs.100

A | C | D
B | B | B
D | A | C

You won Rs.200.
You won on lines: 2

Your current balance is Rs.1100
```

---

## 🧠 Concepts Demonstrated

* Functions
* Loops
* Conditional statements
* Dictionaries
* Lists
* Random number generation
* Nested loops
* Input validation
* Modular programming
* Basic game logic

---

## 🚀 Possible Future Improvements

* Add diagonal winning combinations
* Add jackpots and bonus rounds
* Multiple slot machine themes
* Save player balance using files or a database
* Difficulty levels
* Colored terminal output
* Graphical User Interface (Tkinter or Pygame)
* Sound effects and animations
* Statistics (wins, losses, RTP, total spins)

---

## 📚 Learning Objectives

This project is ideal for beginners learning Python and helps reinforce:

* Working with functions
* Modular programming
* Using the `random` module
* Managing program state
* Building interactive command-line applications
* Writing clean and maintainable code

---

## 📄 License

This project is open-source and available for educational and personal use.

---

## 👨‍💻 Author

**Pranav Sunil Nair**

If you found this project useful, consider giving the repository a ⭐.
