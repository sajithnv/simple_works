from tkinter import *
from functools import partial
t = Tk()
t.geometry('500x690+810+0')
t.title('Calculator Programm')
t['bg']='gray'
t.resizable(0,0)
switch = True
def number(inp):
    global switch
    if inp == 'switch':
        if switch == True:
            on_off.config(bg='green')
            switch = False
            screen_in.config(state='normal')
            screen_in.insert(0,'0')
        else:
            screen_in.config(state='normal')
            screen_in.delete(0,END)
            screen_in.config(state='readonly')
            on_off.config(bg='red')
            switch = True
    if switch == False:
        screen_in.config(state='normal')
        lis_of_oprtr = ['%','/','+','*','-','.']
        lis_of_oprtr1 = ['%','/','+','*']
        lis_of_oprtr2 = ['-','.']
        old_text=screen_in.get()
        if inp.isdigit()==True and old_text == '0' and inp != '00':
            screen_in.delete(0,END)
        if inp in lis_of_oprtr1 and old_text == '0':
            screen_in.delete(0,END)
            screen_in.insert(0,'0')
        if inp == '=':
            old_text=screen_in.get()
            screen_in.delete(0,END)
            screen_in.insert(0,eval(old_text))
        if inp == '<-' and old_text != '0':
            old_text = screen_in.get()
            screen_in.delete(len(old_text)-1,END)
            if len(old_text)==1:
                screen_in.insert(0,'0')
        if inp == 'C':
            screen_in.delete(0,END)
            screen_in.insert(0,'0')
        if inp == '-' and old_text == '0':
            screen_in.delete(0,END)
            screen_in.insert(0,inp)
        if inp == '.' and old_text == '0':
            screen_in.insert(1,inp)
        lis = []
        lis += old_text
        if lis[-1] in lis_of_oprtr and inp in lis_of_oprtr:
            inp = ''
        if inp.isdigit() and inp !='00' or inp in lis_of_oprtr and old_text != '0' or inp == '00' and old_text != '0':
            old_text=screen_in.get()
            screen_in.insert(len(old_text)+1,inp)
        screen_in.config(state='readonly')

top = Frame(t,bd=10,width=400,height=70)
top.place(x=50,y=10)
screen = Frame(t,bg= 'black',bd=10,width=450,height=70)
screen.place(x=26,y=100)
body = Frame(t,bd=20,width=445,height=500,bg='black')
body.place(x=26,y=165)
nums = Frame(body,width=250,height=300,bg='white',bd=15)
nums.place(x=10,y=10)

head_lbl = Label(top,font=('aria',30,'bold'),text='CaLcULaToR',fg='red')
head_lbl.place(x=55,y=0)
screen_in = Entry(screen,width=28,font=('aria',20,'bold'),state='readonly')
screen_in.pack()

on_off = Button(nums,text="ON / OFF",font=('aria',15,'bold'),bd=10,fg='white',bg='red',width=20,command=lambda:number('switch'))
on_off.grid(row=0,column=0,columnspan=4)
btncl = Button(nums,text="C",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('C'))
btncl.grid(row=1,column=0,padx=5,pady=15)
btnpe = Button(nums,text="%",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('%'))
btnpe.grid(row=1,column=1,padx=5)
btnre = Button(nums,text="<-",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('<-'))
btnre.grid(row=1,column=2,padx=5)
btndi = Button(nums,text="/",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('/'))
btndi.grid(row=1,column=3,padx=15)
btn7 = Button(nums,text="7",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('7'))
btn7.grid(row=2,column=0,pady=5)
btn8 = Button(nums,text="8",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('8'))
btn8.grid(row=2,column=1)
btn9 = Button(nums,text="9",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('9'))
btn9.grid(row=2,column=2)
btnmu = Button(nums,text="X",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('*'))
btnmu.grid(row=2,column=3)
btn4 = Button(nums,text="4",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('4'))
btn4.grid(row=3,column=0,pady=5)
btn5 = Button(nums,text="5",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('5'))
btn5.grid(row=3,column=1)
btn6 = Button(nums,text="6",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('6'))
btn6.grid(row=3,column=2)
btnsu = Button(nums,text="-",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('-'))
btnsu.grid(row=3,column=3)
btn1 = Button(nums,text="1",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('1'))
btn1.grid(row=4,column=0,pady=5)
btn2 = Button(nums,text="2",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('2'))
btn2.grid(row=4,column=1)
btn3 = Button(nums,text="3",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('3'))
btn3.grid(row=4,column=2)
btnad = Button(nums,text="+",font=('aria',15,'bold'),bd=10,fg='white',bg='gray',width=4,command=lambda:number('+'))
btnad.grid(row=4,column=3)
btn00 = Button(nums,text="00",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('00'))
btn00.grid(row=5,column=0,pady=5)
btn0 = Button(nums,text="0",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('0'))
btn0.grid(row=5,column=1)
btnpo = Button(nums,text=".",font=('aria',15,'bold'),bd=10,bg='aqua',width=4,command=lambda:number('.'))
btnpo.grid(row=5,column=2)
btneq = Button(nums,text="=",font=('aria',15,'bold'),bd=10,fg='white',bg='red',width=4,command=lambda:number('='))
btneq.grid(row=5,column=3)
t.mainloop()