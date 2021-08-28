from tkinter import *
import time
t= Tk()
t.title('CALCULATOR')
screen = Frame(t,bg="lightblue",width=1600,height=50,relief=SUNKEN)
screen.pack(side=TOP)
localtime = time.asctime(time.localtime(time.time()))
lbl = Label(screen,text = localtime)
lbl.grid(row=0,column=0)
t.mainloop()
