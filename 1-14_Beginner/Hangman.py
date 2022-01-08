from replit import clear
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["Warriors", "Celtics", "Heat", "Lakers"]
chosen_word = random.choice(word_list).lower()
#print(chosen_word)
blank_word = []
for _ in chosen_word:
    blank_word += "_"
#print(blank_word)

end_of_game = False
lifes = 6

while not end_of_game:
    guess_letter = input("Guess a letter: ")
    clear()
    if guess_letter in chosen_word:
        for i in range(len(chosen_word)):
            if guess_letter == chosen_word[i]:
                blank_word[i] = guess_letter
        print(stages[lifes])
    else:
        lifes -= 1
        print(stages[lifes])
    print(blank_word)
    if "_" not in blank_word:
        end_of_game = True
        print("You win.")
    if lifes == 0:
        end_of_game = True
        print("You lose.")
