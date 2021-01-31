from tkinter import *  
from tkinter import messagebox
  
def circle_area():
    name = radius_vvod.get()
    name = int(name)
    name = name*name*3.14
    name = str(name)
    messagebox.showinfo('Count', 'Area is: ' + name)

name = 0

window = Tk()  
window.title('Geometrcic matching:')  
window.geometry('300x250')


radius = Label(window, text="Radius:")  
radius.grid(column=0, row=0)

radius_vvod = Entry(window,width=10)  
radius_vvod.grid(column=1, row=0)

radius_count = Button(window, text="Count", command=circle_area)  
radius_count.grid(column=2, row=0)

window.mainloop()