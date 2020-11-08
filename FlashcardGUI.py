import tkinter as tk
from tkinter import Label, PhotoImage
import pandas
import random

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1500, height = 700)
bgImage = PhotoImage(file = "kyleeQuizlet.png")
background_label = Label(root, image=bgImage)
background_label.place(x=0,y=0)
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
    label1 = tk.Label(root, text=answers[i], bg='white', fg='blue', font=('helvetica', 20, 'bold'), wraplength=1200, justify="center")
    label2= tk.Label(root, text=questions[i], bg='white', fg='red', font=('helvetica', 20, 'bold'), wraplength=1200, justify="center")
    canvas1.create_window(760,240, window=label2)

def showAns():
    global label1
    canvas1.create_window(760,480, window=label1)

global label1
label1 = tk.Label(root, text=answers[i], bg='white', fg='blue', font=('helvetica', 20, 'bold'), wraplength=1200, justify="center")
label2= tk.Label(root, text=questions[i],bg='white', fg='red', font=('helvetica', 20, 'bold'), wraplength=1200, justify="center")
canvas1.create_window(760,240, window=label2)

def rightClick(_):
    newRand()
def downClick(_):
    showAns()

root.bind('<Right>', rightClick)
root.bind('<Down>', downClick)

root.mainloop()