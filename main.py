import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


print(chosen_word)

guess = input("Guess a letter: ")
print(f"You guessed: {guess.lower()}")
# Loop through each letter in the chosen word and ask the user to guess
for x in chosen_word:

    if guess == x:
        print("Right")
    else:
        print("Wrong")
