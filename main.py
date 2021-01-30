from tkinter import *
from subprocess import call
clicks = 0

def click_button():
   call(["python", "calculator.py"])

root = Tk()
root.title('Помощник по математике')
root.geometry("200x350")
root["bg"] = "grey20"
 
btn = Button(text="Калькулятор", background="#292828", foreground="#ccc",
             padx="20", pady="8", font="Arial 16", command=click_button)
btn.pack()
 
root.mainloop()

