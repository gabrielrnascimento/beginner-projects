from random import choice
from csv import reader
# choose a word to be guessed by the user
def chosen_word():
    with open("words.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        print(data)
        word = choice(data)
        return word[0]
    
print(chosen_word())
