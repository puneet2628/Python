from tkinter import *
from textblob import TextBlob



def clear ():
    e1.delete(0,END)
    e2.delete(0,END)

def correction():
    input_word=e1.get()
    blob_obj= TextBlob(input_word)
    corrected_word= str(blob_obj.correct())
    e2.insert(10,corrected_word)
spl=Tk()
spl.geometry("600x300")
spl.title="Spell Corrector "
spl['bg']="#fb7954"

lbl_1=Label(text="Welcome to Spell Correct Application",font="arial 15 bold",background="#fb7954", foreground="black").pack()
lbl_2=Label(text="Input Word",font="arial 10 bold").place(x=20,y=50)

e1= Entry(width=20)
e1.place(x=160,y=50,height=20)

btn_1=Button(spl,text="Correction",font="arial 10 bold",command=correction).place(x=180,y=90)

lbl_3=Label(text="Corrected Word",font="arial 10 bold").place(x=20,y=140)
e2=Entry(width=20)
e2.place(x=160,y=140,height=20)


btn_2=Button(spl,text="Clear",font="arial 10 bold",width=10,bg="#1d9b38",command=clear).place(x=180,y=190)
mainloop()