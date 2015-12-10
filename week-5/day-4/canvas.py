from tkinter import *

master = Tk()
w=Canvas(master, width=400, height=300)
w.pack()

for j in range(4):
    for i in range(4):
        x=40*i
        y=40*j
        w.create_rectangle(0+x, 0+y, 20+x, 20+y, fill='#00ff00')
        w.create_rectangle(20+x, 20+y, 40+x, 40+y, fill='#00ff00')


for n in range(16):
    i=n%4
    j=n//4
    x=40*i
    y=40*j
    w.create_rectangle(0+x, 0+y, 20+x, 20+y, fill='red')
    w.create_rectangle(20+x, 20+y, 40+x, 40+y, fill='red')
mainloop()























print('majom kacsaaaa'  )
