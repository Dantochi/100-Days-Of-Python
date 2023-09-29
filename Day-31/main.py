from tkinter import *
import csv
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
french = []
english = []



# The csv file
with open(file="data/french_words.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    for arr in data:
        french.append(arr[0])
        english.append(arr[1])
        sliced_french = french[1:]
        sliced_english = english[1:]
    print(french)


def word_changer():
    french_word = random.choice(sliced_french)
    global word_index, flip_timer
    window.after_cancel(flip_timer)
    word_index = sliced_french.index(french_word)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(actual_french, text=french_word, fill="black")
    canvas.itemconfig(french_title, text=french[0], fill="black")
    flip_timer = window.after(3000, translator)



def translator():
    english_word = sliced_english[word_index]
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(french_title, text=english[0], fill="white")
    canvas.itemconfig(actual_french, text=english_word, fill="white")
    english.remove(english_word)


# The window config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, translator)

# The card element
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
french_title = canvas.create_text(400, 150, text="French", font=(FONT, 40, "italic"))
actual_french = canvas.create_text(400, 263, text="trouve", font=(FONT, 60, "bold"))
canvas.grid(columnspan=2, row=0)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_back = PhotoImage(file="images/card_back.png")
# Button Element
red_button = Button(image=wrong_image, highlightthickness=0, command=word_changer)
red_button.grid(row=1, column=0)

green_button = Button(image=right_image, highlightthickness=0, command=word_changer)
green_button.grid(row=1, column=1)

file = [french, english]
df = pd.DataFrame(file).transpose()
df.to_csv("data/words_to_learn")

word_changer()

window.mainloop()
