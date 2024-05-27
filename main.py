from tkinter import *
import csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

words = []
with open("data/french_words.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        words.append({"french": row["French"], "english": row["English"]})


def next_card():
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=choice(words)["french"])


canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
# back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

next_card()

window.mainloop()
