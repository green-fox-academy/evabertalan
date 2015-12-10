from tkinter import *

master = Tk()
w=Canvas(master, width=300, height=300)
w.pack()

for i in range(1,151,10):
    a=i
    b=150-i
    w.create_line(a, 150, 150, b, fill='#aad9f9')
    w.create_line(a, 150, 150, b+150, fill='green')
    w.create_line(a+150, 150, 150, b, fill='green')
    w.create_line(a+150, 150, 150, b+150, fill='#aad9f9')


mainloop()
