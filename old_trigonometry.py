from tkinter import *  
from tkinter import messagebox
from tkinter.ttk import Combobox
from trigonometry_defs import *

def calculate():
    func = sincos.get()
    value = value_vvod.get()
    value = float(value)
    if value < 0:
        x = value - 2*value
        x = str(x)
        value = str(value)
        if (func == 'sin') or (func == 'tg') or (func == 'ctg'):
            messagebox.showinfo('Trigonometry', func + '(' + value + ')' + '=' + '-' + func + '(' + x + ')')
        elif func == 'cos':
            messagebox.showinfo('Trigonometry', func + '(' + value + ')' + '=' + func + '(' + x + ')')
            
    elif (value >= 0) and (value <= 90):
        x = 90 - value
        x = str(x)
        value = str(value)
        reverse(func)
        messagebox.showinfo('Trigonometry', func + '(' + value + ')' + '=' + func + '(' + x + ')')
        
        

window = Tk()  
window.title('Geometrcic matching:')  
window.geometry('300x100')


sincos = Combobox(window)  
sincos['values'] = ('sin', 'cos', 'tg', 'ctg')  
sincos.current(1)
sincos.grid(column=0, row=0, padx = 10, pady = 10)

value_vvod = Entry(window,width=10)  
value_vvod.grid(column=1, row=0)

count = Button(window, text="Count", command=calculate)  
count.grid(column=2, row=0)



window.mainloop()