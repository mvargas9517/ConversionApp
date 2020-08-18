from tkinter import *

window=Tk()

def conversion():
    calc=float(e1_value.get()) * 1000,
    calc1=float(e1_value.get()) * 2.20462,
    calc2=float(e1_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, calc)
    t2.delete("1.0", END)
    t2.insert(END, calc1)
    t3.delete("1.0", END)
    t3.insert(END, calc2)




b1=Button(window,text="Convert", command=conversion)
b1.grid(row=1,column=2)

Label(text='Kg').grid(row=0, column=1) 
Label(text='g').grid(row=2, column=1)
Label(text='lbs').grid(row=3, column=1)
Label(text='oz').grid(row=4, column=1)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=2)

t1=Text(window, height=1, width=20)
t1.grid(row=2,column=2)

t2=Text(window, height=1, width=20)
t2.grid(row=3,column=2)

t3=Text(window, height=1, width=20)
t3.grid(row=4,column=2)

window.mainloop()