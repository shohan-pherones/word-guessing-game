import random

word_list = ["vogue", "inheritance", "shikigami", "mascara", "offside"]
hints = {
    "vogue": "Hint: This word is related to style.",
    "inheritance": "Hint: This word is related to programming.",
    "shikigami": "Hint: This word is related to Japanese animation.",
    "mascara": "Hint: This word is related to skincare and makeup.",
    "offside": "Hint: This word is related to a popular sport."
}
chosen_word = random.choice(word_list)
display = ["_" for _ in chosen_word]
lives = 5
game_over = False

print(hints[chosen_word])

while not game_over:
  guess = input("Guess a letter: ").lower()

  if guess in chosen_word:
    for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
  else:
        lives -= 1
        print(f"Incorrect! Lives left: {lives}")

  print(" ".join(display))

  if "_" not in display:
      print("Congratulations! You've guessed the word:", chosen_word)
      game_over = True
  elif lives == 0:
      print("You've run out of lives! The word was:", chosen_word)
      game_over = True