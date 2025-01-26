from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator
root=Tk()
root.geometry("1100x650+100+20")
root.title("Language Translator")
root['bg']='#85e0e0'
root.resizable(False,False)
# TO ADD ADD FUNCTIONALITY IN OUR TRANSLATOR

def tras():
    translate= Translator()
    translate_text= translate.translate(text=input_box.get(1.0,END),src=input_lang.get(),dest=output_lang.get())
    output_box.delete(1.0,END)
    output_box.insert(END,translate_text.text)

# HEADING OF THE PROJECT--------------------------------
heading_lbl = Label(root,text="Language Translator",font="times 15 bold",width=20,bd=2, relief="solid").place(x=440,y=10)
# USER INPUT BLOCK------------------------------------
frm = Frame(root, height=400 , width=400 ,bg="#9933ff", bd=2, relief="solid").place(x=100,y=80)
input_label= Label(root, text="Input Language", width=15,bg="#ffb31a" ,height=2,bd=2, relief="solid",font="times 12 bold").place(x=130,y=100)
languages = list(LANGUAGES.values())
input_lang= ttk.Combobox(root,values=languages,height=10,state='readonly')
input_lang.set("Select Language")
input_box = Text(root, width=40,height=15,bd=2, relief="solid")
input_box.place(x=135,y=180)
input_lang.place(x=310,y=107,height=30)
# USER OUTPUT BOLCK----------------------------------------------
frm1 = Frame(root,height=400 , width=400 ,bg="#9933ff",bd=2, relief="solid").place(x=600,y=80)
output_label= Label(root, text="Output Language", width=15,bg="#ffb31a" ,height=2,bd=2, relief="solid",font="times 12 bold").place(x=630,y=100)
output_lang = ttk.Combobox(root,values=languages,height=10)
output_lang.set("Select Languages")
output_lang.place(x=810,y=107,height=30)
output_box = Text(root, width=40,height=15,bd=2, relief="solid")
output_box.place(x=635,y=180)
# TRANSLATE BUTTON----------------------------------------------
translate_btn = Button(root,text="Translate",width=15,bg="lightgreen" ,height=2, font="times 12 bold",bd=2, relief="solid",command=tras)
translate_btn.place(x=490,y=500)

mainloop()

