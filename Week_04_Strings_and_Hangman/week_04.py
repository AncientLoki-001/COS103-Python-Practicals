# ================= WEEK 4: STRING MANIPULATION AND FORMATTING =================

# Exercise 1: Reverse a string and check for palindrome
# A slice with [::-1] reverses a string. A palindrome reads the same forward and backward.
text = input("Enter a word: ")
reversed_text = text[::-1]

print("Reversed:", reversed_text)

if text.lower() == reversed_text.lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# Exercise 2: Practice string methods
# Common string methods make it easy to change and inspect text.
text = "  Python Programming  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Python", "COS103"))
print(text.strip().split())

# Exercise 3: Simple text-based Hangman
# The program gives the user a few chances to guess a word. It is a basic text version.
word = "python"
guessed = set()
attempts = 6

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

    if guess in word:
        guessed.add(guess)
        print("Good guess!")
    else:
        guessed.add(guess)
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if "".join(letter if letter in guessed else "_" for letter in word) == word:
    print("You win!")
else:
    print("The word was:", word)
