from tkinter import *
from subprocess import call
clicks = 0

def calc():
   call(["python", "calculator.py"])
def match():
   call(['python', 'formulas.py'])

root = Tk()
root.title('Помощник по математике')
root.geometry("200x350")
root["bg"] = "grey20"

calculating = Button(text="Калькулятор", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=calc)
calculating.pack()
matchmaking = Button(text="   Формулы  ", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=match)
matchmaking.pack()


root.mainloop()

