from tkinter import *
from tkinter import messagebox as m
rt  = Tk()
rt.title('TIC-TAC-TOE')
rt.geometry('1000x600+50+50')
rt['bg'] = 'lightblue'
rt.resizable(0,0)

clicked = True
count = 0
def disable_buttons():
    l=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in l:
        i.config(state=DISABLED)
def won():
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' :
        b1.config(fg = 'red')
        b2.config(fg = 'red')
        b3.config(fg = 'red')
        xwin()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' :
        b4.config(fg = 'red')
        b5.config(fg = 'red')
        b6.config(fg = 'red')
        xwin()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' :
        b7.config(fg = 'red')
        b8.config(fg = 'red')
        b9.config(fg = 'red')
        xwin()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' :
        b1.config(fg = 'red')
        b4.config(fg = 'red')
        b7.config(fg = 'red')
        xwin()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' :
        b2.config(fg = 'red')
        b5.config(fg = 'red')
        b8.config(fg = 'red')
        xwin()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' :
        b3.config(fg = 'red')
        b6.config(fg = 'red')
        b9.config(fg = 'red')
        xwin()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' :
        b1.config(fg = 'red')
        b5.config(fg = 'red')
        b9.config(fg = 'red')
        xwin()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' :
        b3.config(fg = 'red')
        b5.config(fg = 'red')
        b7.config(fg = 'red')
        xwin()
        # O wins
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' :
        b1.config(fg = 'red')
        b2.config(fg = 'red')
        b3.config(fg = 'red')
        owin()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' :
        b4.config(fg = 'red')
        b5.config(fg = 'red')
        b6.config(fg = 'red')
        owin()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' :
        b7.config(fg = 'red')
        b8.config(fg = 'red')
        b9.config(fg = 'red')
        owin()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' :
        b1.config(fg = 'red')
        b4.config(fg = 'red')
        b7.config(fg = 'red')
        owin()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' :
        b2.config(fg = 'red')
        b5.config(fg = 'red')
        b8.config(fg = 'red')
        owin()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O' :
        b3.config(fg = 'red')
        b6.config(fg = 'red')
        b9.config(fg = 'red')
        owin()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' :
        b1.config(fg = 'red')
        b5.config(fg = 'red')
        b9.config(fg = 'red')
        owin()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' :
        b3.config(fg = 'red')
        b5.config(fg = 'red')
        b7.config(fg = 'red')
        owin()
    elif count == 9:
        m.showinfo('Oops!!','It\'s a TIE')
        refresh()
def owin():
    c_inp = lblo.cget('text')
    op = int(c_inp)+1
    lblo.config(text=str(op))
    o_name = lbl2.cget('text')
    m.showinfo('info',f'{o_name} SCORE 1 POINT')
    winner(o_name,op)
    refresh()
def xwin():
    c_inp = lblx.cget('text')
    op = int(c_inp)+1
    lblx.config(text=str(op))
    x_name = lbl1.cget('text')
    m.showinfo('info',f'{x_name} SCORE 1 POINT')
    winner(x_name,op)
    refresh()
def winner(name,op):
    if op == 5:
        m.showwarning('GAME OVER !!!',f'player {name} is the winner!!!')
        lblo.config(text='0')
        lblx.config(text='0')
        y = m.askyesno('NEW GAME',"Woul\'d You Like To Play Again ???")
        if y == 1:
            ask_to_change_name()
        else:
            rt.withdraw()
def b_click(b):
    global clicked,count
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        won()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        won()
    else:
        m.showerror('tic-tac-toe','Its not empty !!!!')
def refresh():
    global count
    count = 0
    b=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in b:
        i.config(text=' ')
        i.config(state=ACTIVE)
        i.config(fg='black')
##def exit1():
##    rt.withdraw()
##def minimize():
##    rt.iconify()
def ask_to_change_name():
    x = m.askyesno('player_name','woul\'d you like to change the Name of Players')
    if x == 1:
        change_name()
    else:
        lbl1.config(text = "player 'X' :")
        lbl2.config(text = "player 'O' :")
def change_name():
    def save_name():
        new_x = p_entry1.get()
        new_o = p_entry2.get()
        lbl1.config(text = new_x.upper()+' (X):')
        lbl2.config(text = new_o.upper()+' (O):')
        t.withdraw()
    global p_entry1,p_entry2
    t=Tk()
    t.geometry('690x150+550+200')
    t.title('Change Player_Names')
    top1 = Frame(t,bg = 'lightgreen',bd=20)
    top1.pack(side=TOP)
    player1 = Label(top1,text="player 'X'  :",font=('aria',20,'bold'),width=20)
    player2 = Label(top1,text="player 'O'  :",font=('aria',20,'bold'),width=20)
    p_entry1 = Entry(top1,font=('aria',20,'bold'),width=20)
    p_entry2 = Entry(top1,font=('aria',20,'bold'),width=20)
    btn = Button(top1,text='SAVE',command = save_name,font=('aria',10,'bold'),width=10,relief=SUNKEN,bg='red',fg='white')
    player1.grid(row=1,column=1)
    player2.grid(row=2,column=1)
    p_entry1.grid(row=1,column=2)
    p_entry2.grid(row=2,column=2)
    btn.grid(row=3,column=2)
    t.mainloop()
    
top = Frame(rt,bg="white",width=500,height=50,bd=20)
top.place(x=300,y=10)
player = Frame(rt,bg="lightblue",width=500,height=500,bd=20)
player.place(x=500,y=350)
game = Frame(rt,bg="red",width=500,height=500,bd=20,relief=SUNKEN)
game.place(x=100,y=150)

lbl1 = Label(player,text="player 'X'  : ",font=('aria',20,'bold'),width=20,bd=10)
lblx = Label(player,text='0',font=('aria',20,'bold'),fg= 'red',bd=10)
lbl2 = Label(player,text="player 'O'  : ",font=('aria',20,'bold'),width=20,bd=10)
lblo = Label(player,text='0',font=('aria',20,'bold'),fg= 'red',bd=10)
lbl1.grid(row=2,column=0)
lbl2.grid(row=3,column=0)
lblx.grid(row=2,column=1)
lblo.grid(row=3,column=1)

head=Label(top,font=('aria',30,'bold'),text="TIC _ TAC _ TOE")
head.grid(row=0,column=0)
##reset_btn = Button(game,text = 'Refresh',command = lambda :refresh(),width=14,bg='black',fg='white')
##reset_btn.grid(row=4,column=0)
##exit_btn = Button(game,text = 'Exit',command = lambda :exit1(),width=14,bg='black',fg='white')
##exit_btn.grid(row=4,column=1)
##minimize_btn = Button(game,text = 'Minimize',command = lambda :minimize(),width=14,bg='black',fg='white')
##minimize_btn.grid(row=4,column=2)
b1=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b1))
b2=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b2))
b3=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b3))

b4=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b4))
b5=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b5))
b6=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b6))

b7=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b7))
b8=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b8))
b9=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b9))

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
ask_to_change_name()
rt.mainloop()
