import random

stages = ['''
  +---+
  |   |
      |
      |
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
  O   |
  |   |
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
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]


lives = 6

chosen_word = random.choice(word_list)


print(chosen_word)

word_length = len(chosen_word)
placeholder = ""

for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letter = []

game_over = False

while not game_over:

    print(f"******************{lives}/6 LIVES LEFT*******************")
    guess = input("Guess a letter: ")
    print(f"You guessed: {guess.lower()}")
# Loop through each letter in the chosen word and ask the user to guess
    if guess in correct_letter:
        print(f"You've already guessed {guess}")

    display = ""

    for x in chosen_word:

        if guess == x:
            display += x
            correct_letter.append(guess)
        elif x in correct_letter:
            display += x
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"******************IT WAS {chosen_word}! YOU LOSE*******************")

    if "_" not in display:
        game_over = True
        print("*******************YOU WIN************************")

    print(stages[lives])