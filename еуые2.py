from tkinter import *
import tkinter as tk
import pyodbc

root1 = tk.Tk()

label1 = tk.Label(root1, text='product A')
entry1 = tk.Entry(root1)

label1.pack(side = tk.TOP)
entry1.pack()
input1= StringVar()
input1.set(entry1.get())
print (input1)