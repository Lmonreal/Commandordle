import os
import random
import colorama

chosen_word = ""
dssmbled_word = []
guesses = 1
words = []
win_condition = False

dssmbled_guesses = {
    "dg1": [],
    "dg2": [],
    "dg3": [],
    "dg4": [],
    "dg5": [],
    "dg6": []
}

number_guess = {
    "g1": "",
    "g2": "",
    "g3": "",
    "g4": "",
    "g5": "",
    "g6": ""
}


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open('filteredwords.txt', 'r') as file:
        words = file.readlines()
        item = 0
        for word in words:
            words[item] = word.rstrip()
            item += 1
        chosen_word = random.choice(words)
except:
    print("ERROR: Cannot open filteredwords.txt")

for char in chosen_word:
    dssmbled_word.append(char)



def colored_answer(input):
    index = 0
    for char in input:
        if char == dssmbled_word[index]:
            print(colorama.Fore.GREEN + f"{char}" + colorama.Fore.RESET, end=" ")
        elif char in dssmbled_word:
            print(colorama.Fore.YELLOW + f"{char}" + colorama.Fore.RESET, end=" ")
        else:
            print(colorama.Fore.RED + f"{char}" + colorama.Fore.RESET, end=" ")
        
        index += 1
    print()

# Guess Logic. Looks for valid word
def guess():
    while True:
        user_guess = (input(f"Please enter guess n{guesses}: ")).upper()
        if user_guess in words:
            break
        else:
            print(f"{user_guess} is not a valid word. Please Try again.")

    return user_guess


while guesses <= 6:
    number_guess[f"g{guesses}"] = guess()
    for char in number_guess[f"g{guesses}"]:
        dssmbled_guesses[f"dg{guesses}"].append(char)

    clear_terminal()
    if number_guess[f"g{guesses}"] == chosen_word:
        win_condition = True
        break

    # Checking individual letter logic

    for value in range(1, (guesses+1)):
        colored_answer(dssmbled_guesses[f"dg{value}"])

    guesses += 1


colored_answer(dssmbled_word)
if win_condition == True:
    print("Congrats! You Won!")
else:
    print("You Lose! Try Again.")