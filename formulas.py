from tkinter import *  
from tkinter import messagebox
from math import hypot
from PIL import ImageTk, Image
import os
  
def circle_area():
    name = radius_vvod.get()
    name = int(name)
    name = name*name*3.14
    name = str(name)
    messagebox.showinfo('Circle Area', 'Area is: ' + name)
    
def length_area():
    leng = length_vvod.get()
    leng = int(leng)
    leng = leng*2*3.14
    leng = str(leng)
    messagebox.showinfo('Length Circle', 'Length is: ' + leng)
    
def vector_length():
    x = vectorx_vvod.get()
    y = vectory_vvod.get()
    x = int(x)
    y = int(y)
    ans = hypot(x,y)
    ans = str(ans)
    messagebox.showinfo('Vector Length', 'Length is: ' + ans)
    
name = 0

window = Tk()  
window.title('Geometrcic matching:')  
window.geometry('235x190')

############################################################

radius_title = Label(window, text="1) Circle's area")  
radius_title.grid(column=0, row=0)

radius = Label(window, text="Radius:", padx = 0)  
radius.grid(column=0, row=1)

radius_vvod = Entry(window,width=10)  
radius_vvod.grid(column=1, row=1)

radius_count = Button(window, text="Count", command=circle_area)  
radius_count.grid(column=2, row=1)

############################################################

length_title = Label(window, text="    2) Circle's length")  
length_title.grid(column=0, row=3, padx = 0)

length = Label(window, text="Radius:")  
length.grid(column=0, row=4)

length_vvod = Entry(window,width=10)  
length_vvod.grid(column=1, row=4)

length_count = Button(window, text="Count", command=length_area)  
length_count.grid(column=2, row=4)

############################################################

vector_title = Label(window, text=" 3) Hypotenuse")  
vector_title.grid(column=0, row=5, padx = 0)

vectorx = Label(window, text="Leg 1:")  
vectorx.grid(column=0, row=6)

vectorx_vvod = Entry(window,width=10)  
vectorx_vvod.grid(column=1, row=6)

vectory = Label(window, text="Leg 2:")  
vectory.grid(column=0, row=8)

vectory_vvod = Entry(window,width=10)  
vectory_vvod.grid(column=1, row=8)

vector_count = Button(window, text="Count", command=vector_length)  
vector_count.grid(column=2, row=6)

############################################################

window.mainloop()