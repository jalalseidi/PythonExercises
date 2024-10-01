import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


print(chosen_word)

word_length = len(chosen_word)
placeholder = ""

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ")
print(f"You guessed: {guess.lower()}")
# Loop through each letter in the chosen word and ask the user to guess

display = ""

for x in chosen_word:

    if guess == x:
        display += x
    else:
        display += "_"
print(display)