from tkinter import *

cal = Tk()
cal.geometry("300x395")
cal.title("calculator")
cal['bg']="#1B1212"

def click(num):
    value=e.get()
    e.delete(0,END)
    e.insert(0,str(value)+str(num))
def clear():
    e.delete(0,END)

def add():
    num=e.get()
    e.delete(0,END)
    global math
    math="add"
    global a
    a=int(num)

def sub():
    num1=e.get()
    e.delete(0,END)
    global math
    math="sub"
    global b 
    b = int(num1)

def mult():
    num2=e.get()
    e.delete(0,END)
    global math
    math = "mult"
    global c
    c= int(num2)

def divi():
    num3=e.get()
    e.delete(0,END)
    global math
    math = "divi"
    global d
    d= int(num3)

def equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,a+int(second))
    elif math=="sub":
        e.insert(0,b-int(second))
    elif math=="mult":
        e.insert(0,c*int(second))
    elif math=="divi":
        e.insert(0,d/ int(d))


e = Entry(cal,width=46,bg="lightgrey")
e.place(x=10,y=10,height=30)


btn_0 = Button(cal,text="C",font="arial 18 bold",width=3,fg="white",bg="#FF5733",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=clear).place(x=10,y = 50)
btn_1 = Button(cal,text="AC",font="arial 18 bold",width=3,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=clear).place(x=85,y = 50)
btn_2 = Button(cal,text="/",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=divi).place(x=160,y = 50)
btn_3 = Button(cal,text="x",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=mult).place(x=235,y = 50)

btn_4 = Button(cal,text="7",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(7)).place(x=10,y = 120)
btn_5 = Button(cal,text="8",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(8)).place(x=85,y = 120)
btn_6 = Button(cal,text="9",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(9)).place(x=160,y = 120)
btn_7 = Button(cal,text="-",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=sub).place(x=235,y = 120)

btn_8 = Button(cal,text="4",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(4)).place(x=10,y = 190)
btn_9 = Button(cal,text="5",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(5)).place(x=85,y = 190)
btn_10 = Button(cal,text="6",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(6)).place(x=160,y = 190)
btn_11 = Button(cal,text="+",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=add).place(x=235,y = 190)

btn_12 = Button(cal,text="1",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(1)).place(x=10,y = 260)
btn_13= Button(cal,text="2",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(2)).place(x=85,y = 260)
btn_14= Button(cal,text="3",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(3)).place(x=160,y = 260)

btn_15 = Button(cal,text="0",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(0)).place(x=10,y = 330,width=130)
btn_16= Button(cal,text=".",font="arial 18 bold",width=3,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white").place(x=160,y = 330)
btn_17= Button(cal,text="=",font="arial 18 bold",width=3,bg="orange",fg="white",cursor="hand2",activebackground="orange",activeforeground="white",command=equal).place(x=235,y = 260,height=122)

mainloop()


