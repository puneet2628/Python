from tkinter import *

cal=Tk()
cal.geometry("350x450")
cal.title("Calculator")
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
    b=int(num1)
def multi():
    num2=e.get()
    e.delete(0,END)
    global math
    math="multi"
    global c
    c=int(num2)
def divi():
    num3=e.get()
    e.delete(0,END)
    global math
    math="divi"
    global d
    d=int(num3)
# conversion______________________
def usddollar():
    number=e.get()
    e.delete(0,END)
    cov=float(number)
    e.insert(0,cov*83.95)
def inrrupee():
    number1=e.get()
    e.delete(0,END)
    cov1=float(number1)
    e.insert(0,cov1*1)

def ausdollar():
    number2=e.get()
    e.delete(0,END)
    cov2=float(number2)
    e.insert(0,cov2*56.516)

def japyen():
    number3=e.get()
    e.delete(0,END)
    cov3=float(number3)
    e.insert(0,cov3*0.564997)

def sindollar():
    number4=e.get()
    e.delete(0,END)
    cov4 = float(number4)
    e.insert(0,cov4*64.128)

def sarand():
    number5=e.get()
    e.delete(0,END)
    cov5=float(number5)
    e.insert(0,cov5*4.779214)

def pakrupee():
    number6=e.get()
    e.delete(0,END)
    cov6=float(number6)
    e.insert(0,cov6*0.302132)

def newzelanddollar():
    number7=e.get()
    e.delete(0,END)
    cov7=float(number7)
    e.insert(0,cov7*50.982203)

# equal to______________________________
def equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,a+int(second))
    elif math=="sub":
        e.insert(0,b-int(second))
    elif math=="multi":
        e.insert(0,c* int(second))
    elif math=="divi":
        e.insert(0,d/int(second))
e = Entry(cal,width=54,bg="lightgrey")
e.place(x=10,y=10,height=35)
btn_0 = Button(cal,text="1",font="arial 18 bold",width=4,fg="white",bg="#343434",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(1)).place(x=10,y =60 )
btn_1 = Button(cal,text="2",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(2)).place(x=98,y =60 )
btn_2 = Button(cal,text="3",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(3)).place(x=185,y=60)
btn_3 = Button(cal,text="4",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(4)).place(x=270,y=60)
btn_4 = Button(cal,text="5",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(5)).place(x=10,y=125)
btn_5 = Button(cal,text="6",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(6)).place(x=98,y=125)
btn_6 = Button(cal,text="7",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(7)).place(x=185,y=125)
btn_7 = Button(cal,text="8",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(8)).place(x=270,y=125)
btn_8 = Button(cal,text="9",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(9)).place(x=10,y=190)
btn_9 = Button(cal,text="0",font="arial 18 bold",width=4,bg="#343434",fg="white",cursor="hand2",activebackground="#343434",activeforeground="white",command=lambda:click(0)).place(x=98,y=190)
btn_10 = Button(cal,text="Clear",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=clear).place(x=185,y=190)
btn_11= Button(cal,text="=",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=equal).place(x=270,y=190)

btn_12 = Button(cal,text="+",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=add).place(x=10,y=255)
btn_13 = Button(cal,text="-",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=sub).place(x=98,y=255)
btn_14 = Button(cal,text="*",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=multi).place(x=185,y=255)
btn_15 = Button(cal,text="/",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=divi).place(x=270,y=255)

btn_16 = Button(cal,text="INR",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=inrrupee).place(x=10,y=320)
btn_17 = Button(cal,text="USD",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=usddollar).place(x=98,y=320)
btn_18 = Button(cal,text="AUS",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=ausdollar).place(x=185,y=320)
btn_19 = Button(cal,text="JPY",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=japyen).place(x=270,y=320)

btn_20 = Button(cal,text="SGD",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=sindollar).place(x=10,y=385)
btn_21 = Button(cal,text="SAR",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=sarand).place(x=98,y=385)
btn_22 = Button(cal,text="PKR",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=pakrupee).place(x=185,y=385)
btn_23 = Button(cal,text="NZD",font="arial 18 bold",width=4,bg="#FF5733",fg="white",cursor="hand2",activebackground="#FF5733",activeforeground="white",command=newzelanddollar).place(x=270,y=385)




mainloop()