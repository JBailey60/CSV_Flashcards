import tkinter as tk
from tkinter import Label
import pandas
import random

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1500, height = 700)
canvas1.pack()

foo = pandas.read_csv("Flashcards.csv")
questions = foo.questions
answers = foo.answers
i = random.randint(0, len(questions)-1)


def newRand():
    global i  
    i = random.randint(0,len(questions)-1)
    global label2
    label2.destroy()
    global label1
    label1.destroy()
    label1 = tk.Label(root, text=answers[i], fg='green', font=('helvetica', 20, 'bold'), wraplength=750, justify="center")
    label2= tk.Label(root, text=questions[i], fg='red', font=('helvetica', 20, 'bold'), wraplength=750, justify="center")
    canvas1.create_window(750,100, window=label2)

def showAns():
    global label1
    canvas1.create_window(750,400, window=label1)

global label1
label1 = tk.Label(root, text=answers[i], fg='green', font=('helvetica', 20, 'bold'), wraplength=750, justify="center")
label2= tk.Label(root, text=questions[i], fg='red', font=('helvetica', 20, 'bold'), wraplength=750, justify="center")
canvas1.create_window(750,100, window=label2)


# button1 = tk.Button(text='Answer',command=showAns, bg='brown',fg='white')
# canvas1.create_window(150, 150, window=button1)

# button2 = tk.Button(text="Next", command=newRand)
# canvas1.create_window(200, 150, window=button2)

def rightClick(_):
    newRand()
def downClick(_):
    showAns()


root.bind('<Right>', rightClick)
root.bind('<Down>', downClick)

root.mainloop()