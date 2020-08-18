from random import choice
from csv import reader

hangman = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")


# choose a word to be guessed by the user
def chosen_word():
    with open("words.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        word = choice(data)
        return word[0]

# check if letter is inside word
def check_letter(letter, word):
    if letter in word.lower():
        return True
    return False

# displays the word with an asterisk until the player chooses a letter the word contains
def word_status(word, letters_used):
    test = ''.join([" " if letter == " " else letter if letter.lower() in letters_used else "*" for letter in word])
    return test

# check if the guesses completed the word
def check_word(word, letters_used):
    letters_in_word = [letter.lower()  for letter in word if letter.isalnum()]
    right_letters = []
    for i in word.lower():
        if i in letters_used:
            right_letters.append(i)
    if len(letters_in_word) == len(right_letters):
        return True
    return False

run = True
while run:
    won = False
    letters_used = []
    word = chosen_word()
    round_count = 0
    while round_count < 10 and won == False:
        print(hangman[round_count])
        print(word_status(word, letters_used))
        # print(word)
        letter = input("Choose a letter: ")
        letters_used.append(letter)
        if check_letter(letter, word):
            if check_word(word, letters_used):
                print(f"You guessed right! The country is {word}!")
                break
        else:
            round_count += 1
    else:
        print(f"You got hanged! The country is {word}!")
    replay = input("Do you want to play again? (Y/N) ?\n")
    if replay.lower() in ['y', 'yes']:
        run = True
    else:
        run = False