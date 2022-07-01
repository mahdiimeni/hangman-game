# Guess Game ---> Angela Yu's Python bootcamp course - Day 7
# My solution

import random
from hangman_art import logo, stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
lives = 6
display = ["_" for _ in range(len(chosen_word))]

print(logo)
print()

while "_" in display:
    guess = input(" -- Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed letter -{guess}- !")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"The letter -{guess}- is not in the word! - You lose a live!")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("Game Over!!")
            break

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        print("\nYou Win")
        break