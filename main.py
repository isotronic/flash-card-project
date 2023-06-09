from tkinter import *
from tkinter import messagebox
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
word_pair = {}

try:
    word_list = read_csv("data/words_to_learn.csv").to_dict(orient="records")
except errors.EmptyDataError:
    messagebox.showinfo(title="Oops", message="You have learnt all the remaining words.\n "
                                              "The original list has been loaded, so you can start from the beginning")
    word_list = read_csv("data/french_words.csv").to_dict(orient="records")
except FileNotFoundError:
    word_list = read_csv("data/french_words.csv").to_dict(orient="records")


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global word_pair
    title = list(word_pair.keys())[1]
    word = word_pair["English"]

    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text=title, fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")


# ---------------------------- GENERATE NEW CARD ------------------------------- #
def next_card():
    global timer
    global word_pair
    word_pair = choice(word_list)
    title = list(word_pair.keys())[0]
    word = word_pair["French"]

    window.after_cancel(timer)

    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text=title, fill="black")
    canvas.itemconfig(word_text, text=word, fill="black")

    timer = window.after(3000, flip_card)


# ---------------------------- CARD IS KNOWN ------------------------------- #
def card_known():
    global word_list
    word_list.remove(word_pair)

    data = DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

timer = window.after(3000, flip_card)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=card_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
