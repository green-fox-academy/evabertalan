from tkinter import *

master = Tk()
w=Canvas(master, width=2000, height=2000)
w.pack()


for i in range(1,1001,20):
    a=i
    b=1000-i
    w.create_line(a, 0, 0, b, fill='#aad9f9')



mainloop()
