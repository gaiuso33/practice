import random
def choose_word():
    words = ["python", "programming", "computer", "science", "algorithm", "database", "network", "software"]
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
def hangman():
    word = choose_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()  # what the user has guessed
    lives = 6
    # Game loop
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(guessed_letters))
        # What current word is (ie W - R D)
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")
    # Game ended
    if lives == 0:
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")
if __name__ == "__main__":
    hangman()