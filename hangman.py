import tkinter as tk
import random

# Word list
words = ["apple", "python", "gamer", "train", "code"]
chosen_word = random.choice(words)
display_word = ["_"] * len(chosen_word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Hangman drawing steps
def draw_hangman(wrong):
    if wrong == 1:
        canvas.create_oval(90, 50, 130, 90)  # Head
    elif wrong == 2:
        canvas.create_line(110, 90, 110, 150)  # Body
    elif wrong == 3:
        canvas.create_line(110, 100, 90, 130)  # Left Arm
    elif wrong == 4:
        canvas.create_line(110, 100, 130, 130)  # Right Arm
    elif wrong == 5:
        canvas.create_line(110, 150, 90, 180)  # Left Leg
    elif wrong == 6:
        canvas.create_line(110, 150, 130, 180)  # Right Leg

# Guess handler
def guess_letter():
    global wrong_guesses
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        result_label.config(text="Enter a single alphabet.")
        return

    if letter in guessed_letters:
        result_label.config(text="You already guessed that.")
        return

    guessed_letters.append(letter)

    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                display_word[i] = letter
        word_label.config(text=" ".join(display_word))
        result_label.config(text="Correct!")
    else:
        wrong_guesses += 1
        draw_hangman(wrong_guesses)
        result_label.config(text=f"Wrong! {max_wrong - wrong_guesses} lives left.")

    if "_" not in display_word:
        result_label.config(text="🎉 You win!")
        guess_button.config(state="disabled")
    elif wrong_guesses == max_wrong:
        result_label.config(text=f"💀 You lose! Word was: {chosen_word}")
        guess_button.config(state="disabled")

# Setup GUI
root = tk.Tk()
root.title("Hangman Game")
root.geometry("300x400")
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(pady=10)

# Gallows
canvas.create_line(20, 180, 180, 180)  # Base
canvas.create_line(50, 180, 50, 20)    # Pole
canvas.create_line(50, 20, 110, 20)    # Top bar
canvas.create_line(110, 20, 110, 50)   # Rope

word_label = tk.Label(root, text=" ".join(display_word), font=("Courier", 18))
word_label.pack()
entry = tk.Entry(root, font=("Courier", 14))
entry.pack()
guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
