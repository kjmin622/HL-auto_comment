from tkinter import *
from tkinter import ttk
import create

def main():
    window =Tk()

    window.title("HL_AUTO_COMMENT")
    window.geometry("250x300")
    window.resizable(0,0)
    #window.resizeable(False,False)
    name = StringVar()
    hakga = StringVar()
    ans=StringVar()

    answer = Text(window)


    def click(event):
        answer.delete(1.0,END)
        str = (create.create(name.get(),hakga.get()))
        answer.insert(CURRENT,str)

    label1 = ttk.Label(window,text="     이름: ")
    label2 = ttk.Label(window,text="     학과: ")
    space1 = ttk.Label(window,text=" ")
    space2 = ttk.Label(window,text=" ")
    space3 = ttk.Label(window,text=" ")
    textbox1 = ttk.Entry(window,width=22,textvariable=name)
    textbox2 = ttk.Entry(window,width=22,textvariable=hakga)
    
    space1.grid(column=0,row=0)

    label1.grid(column=0,row=1)
    textbox1.grid(column=1,row=1)

    space2.grid(column=0,row=2)

    label2.grid(column=0,row=3)
    textbox2.grid(column=1,row=3)

    space3.grid(column=0,row=4)
    
    window.bind('<Return>',click)
    
    answer.place(x=10,y=120,width=230,height=170)
    window.mainloop()

main()
