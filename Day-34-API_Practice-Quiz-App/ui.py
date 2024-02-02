from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # The helps to specify the datatype of the parameter
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 13, 'bold'))
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'), width=280)
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")
        self.green = Button(image=self.right_image, command=self.green, highlightthickness=0)
        self.green.grid(row=2, column=0)
        self.red = Button(image=self.wrong_image, command=self.red, highlightthickness=0)
        self.red.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've resched the end of the quiz")
            self.red.config(state="disabled")
            self.green.config(state="disabled")

    def green(self):
        is_right = self.quiz.check_answer("True")
        return self.give_feedback(is_right)

    def red(self):
        is_right = self.quiz.check_answer("False")
        return self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

