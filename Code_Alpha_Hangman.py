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

# Main game loop
while incorrect_guesses < max_attempts:
    # Display the current progress of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    # Check if the user has guessed the whole word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.\n")
        continue

    # Check for duplicate guesses
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!\n")

# Game over condition
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)
