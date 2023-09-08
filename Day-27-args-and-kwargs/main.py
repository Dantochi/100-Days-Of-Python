from tkinter import *

window = Tk()  # Used to create the GUI Window
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# pack() is used to display a widget on the GUI
# place() is used for precision positioning on the GUI through its x and y parameters
# grid() is used for positioning using column and row parameters
# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=3)  # Required to display the label


# args represents many positional arguments
# Kwargs represents many or optional keyword arguments
# To display anything in the GUI the .pack() method has to be used
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=50)  # Used to create an input box in the GUI
input.grid(column=0, row=0)
print(input.get())

window.mainloop()  # Keeps the GUI Open
