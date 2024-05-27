from tkinter import *
import csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

words = []
try:
    with open("data/words_to_learn.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append({"French": row["French"], "English": row["English"]})
except FileNotFoundError:
    with open("data/french_words.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append({"French": row["French"], "English": row["English"]})


def next_card(arg):
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words)
    if arg == 1:
        words.remove(current_card)
        with open("data/words_to_learn.csv", "w", newline="") as data_file:
            writer = csv.DictWriter(data_file, fieldnames=["French", "English"])
            writer.writeheader()
            writer.writerows(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=lambda: next_card(1))
button_right.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=lambda: next_card(2))
button_wrong.grid(row=1, column=0)

next_card(3)

window.mainloop()
