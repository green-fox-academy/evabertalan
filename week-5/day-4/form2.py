from tkinter import *

master = Tk()
w=Canvas(master, width=300, height=300)
w.pack()

for i in range(1,151,5):
    a=i
    b=150-i
    w.create_line(a, 150, 150, b, fill='#00FFFF')
    w.create_line(a, 150,150, a+150, fill='#FF00FF')
    w.create_line(a+150, 150, 150, b+150, fill='#00FFFF')
    w.create_line(a+150, 150, 150, a, fill='#FF00FF')


mainloop()
