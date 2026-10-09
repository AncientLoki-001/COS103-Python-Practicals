# WEEK 4: STRINGS AND HANGMAN
text = input("Enter a word: ")
reversed_text = text[::-1]
print("Reversed:", reversed_text)
print("It is a palindrome." if text.lower() == reversed_text.lower() else "It is not a palindrome.")

text = "  Python Programming  "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Python", "COS103"))
print(text.strip().split())

word, guessed, attempts = "python", set(), 6
while attempts > 0:
    display = "".join(letter if letter in guessed else "_" for letter in word)
    print("Word:", display)
    if display == word:
        print("You win!")
        break
    guess = input("Guess one letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.add(guess)
    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)
if "".join(letter if letter in guessed else "_" for letter in word) == word:
    print("You win!")
else:
    print("The word was:", word)
