from tkinter import *
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
WORD_LIST = read_csv("data/french_words.csv").to_dict(orient="records")


# ---------------------------- GENERATE NEW CARD ------------------------------- #
def next_card():
    word_pair = choice(WORD_LIST)
    title = list(word_pair.keys())[0]
    word = word_pair["French"]

    canvas.itemconfig(title_text, text=title)
    canvas.itemconfig(word_text, text=word)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
