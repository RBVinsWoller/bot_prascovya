from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Reduction Formulas')

img = ImageTk.PhotoImage(Image.open("1.jpeg"))

panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()