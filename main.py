import random

word_list = ["aardvark", "baboon", "camel"]

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
    guess = input("Guess a letter: ")
    print(f"You guessed: {guess.lower()}")
# Loop through each letter in the chosen word and ask the user to guess

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

    if "_" not in display:
        game_over = True
        print("You Win.")