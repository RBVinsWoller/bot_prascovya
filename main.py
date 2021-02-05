from tkinter import *
from subprocess import call

def calc():
   call(["python", "calculator.py"])
def match():
   call(['python', 'formulas.py'])
def rooty():
   call(['python', 'roots.py'])   
def trigonometry():
   call(['python', 'trigonometry.py'])   

root = Tk()
root.title('�������� �� ����������')
root.geometry("200x350")
root["bg"] = "grey20"

calculating = Button(text="�����������", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=calc)
calculating.pack()

matchmaking = Button(text="   �������  ", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=match)
matchmaking.pack()

rootsy = Button(text="     �����     ", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=rooty)
rootsy.pack()

trigonometry = Button(text="����������", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=trigonometry)
trigonometry.pack()


root.mainloop()

