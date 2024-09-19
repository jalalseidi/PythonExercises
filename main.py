import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


print(f"The chosen word has {len(chosen_word)} letters.")

# Loop through each letter in the chosen word and ask the user to guess
for x in chosen_word:
    guess = input("Guess a letter: ")
    print(f"You guessed: {guess}")
