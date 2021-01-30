from tkinter import *
from subprocess import call
clicks = 0

def click_button():
   call(["python", "calculator.py"])

root = Tk()
root.title('Помощник по математике')
root.geometry("400x250")
 
btn = Button(text="Калькулятор", background="#dabdab", foreground="#000",
             padx="20", pady="8", font="Arial 16", command=click_button)
btn.pack()
 
root.mainloop()