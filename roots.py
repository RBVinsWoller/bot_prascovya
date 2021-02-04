from tkinter import *  
from tkinter import messagebox
from math import *
  
def root_2():
    name = r2_vvod.get()
    name = int(name)
    name = sqrt(name)
    name = str(name)
    messagebox.showinfo('Root 2', 'Root is ' + name)
    
def root_3():
    name = r3_vvod.get()
    name = int(name)
    name = name**(1./3)
    name = str(name)
    messagebox.showinfo('Root 3', 'Root is '+ name)
    
def root_n():
    rNx = rNx_vvod.get()
    rNy = rNy_vvod.get()
    rNx = int(rNx)
    rNy = int(rNy)
    ans = rNx**(1./rNy)
    ans = str(ans)
    messagebox.showinfo('Root N', 'Root is: ' + ans)

window = Tk()  
window.title('Root matching:')  
window.geometry('190x200')

############################################################

r2_title = Label(window, text="1) Root 2")  
r2_title.grid(column=0, row=0)

r2 = Label(window, text="Number:", padx = 10)  
r2.grid(column=0, row=1)

r2_vvod = Entry(window,width=10)  
r2_vvod.grid(column=1, row=1)

r2_count = Button(window, text="Count", command=root_2)  
r2_count.grid(column=2, row=1)

############################################################

r3_title = Label(window, text="2) Root 3")  
r3_title.grid(column=0, row=3, padx = 0)

r3 = Label(window, text="Number:")  
r3.grid(column=0, row=4)

r3_vvod = Entry(window,width=10)  
r3_vvod.grid(column=1, row=4)

r3_count = Button(window, text="Count", command=root_3)  
r3_count.grid(column=2, row=4)

############################################################

rN_title = Label(window, text="3) Root N")  
rN_title.grid(column=0, row=5, padx = 0)

rNx = Label(window, text="Number:")  
rNx.grid(column=0, row=6)

rNx_vvod = Entry(window,width=10)  
rNx_vvod.grid(column=1, row=6)

rNy = Label(window, text="Root:")  
rNy.grid(column=0, row=8)

rNy_vvod = Entry(window,width=10)  
rNy_vvod.grid(column=1, row=8)

rN_count = Button(window, text="Count", command=root_n)  
rN_count.grid(column=2, row=6)

############################################################

window.mainloop()