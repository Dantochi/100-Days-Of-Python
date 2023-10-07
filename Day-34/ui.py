from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score = Label(text="Score: 0", pady=20)
        self.question = Label(text="", bg='white', font=('Arial', 20, 'italic'), height=250, width=300, padx=20)
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")
        self.green = Button(image=self.right_image, command="")
        self.red = Button(image=self.wrong_image, command="")
        self.window.mainloop()
