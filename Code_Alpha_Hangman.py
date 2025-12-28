import random

# List of predefined words
word_list = ["python", "java", "apple", "chair", "music","computer","keyboard","phone","screen","flower","garden","forest","cloud","deploy","bugs","developer","tester","brushup","stress","knowledge","priority","jumbling","camera","bottle","window","school","college","student","teacher","notebook",]

# Randomly select a word
secret_word = random.choice(word_list)

# Variables initialization
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

