from googletrans import Translator
from gtts import gTTS
from tkinter import *
from PIL import Image,ImageTk
 
window=Tk()

window.geometry('600x280')
window.config(bg="black")
image=Image.open("piyush.jpg")
photo=ImageTk.PhotoImage(image)
b=Label(window,image=photo)
b.place(x=0,y=-50)
# b.pack()
el=Entry(window,bg="white",fg="black",font=("Arial",25,"bold"))
el.place(x=20,y=20)
# set=PhotoImage(file="ak1.png")
# Label_1=Label(window,image=set)
# Label_1.place(x=0,y=-50)
def convert_language():
    a1=el.get()
    t1=Translator()
    t2=click_option.get()

    if t2=="English":
        convert="en"
    elif t2=="Hindi":
        convert="hi"
    elif t2=="German":
        convert="de"
    elif t2=="French":
        convert="fr"
    elif t2=="Spanish":
        covert="es"
    elif t2=="Russian":
        convert="ru"
    trans_text=t1.translate(a1,dest=convert)
    trans_text=trans_text.text
    ob1=gTTS(text=trans_text,slow=False,lang=convert)
    label_2.config(text=trans_text)
choices=[
    "English",
    "Hindi",
    "German",
    "French",
    "Spanish",
    "Russian"
] 
click_option=StringVar()
click_option.set("Select Language")

List_drop=OptionMenu(window,click_option,*choices)
List_drop.configure(background="green",foreground="white",font=('Arial',15,"bold"))
List_drop.place(x=400,y=20)

label_2=Label(window,text="\t\t\t\t\t\t",bg="black",fg="white",font=("Arial",40,"bold"))
label_2.place(x=0,y=120)
label_2=Label(window,text="Translated text",bg="black",fg="white",font=("Arial",40,"bold"))
label_2.place(x=180,y=120)
Button=Button(window,text="Translate",bg="red",fg="white",font=("Arial",25,"bold"),command=convert_language)
Button.place(x=220,y=200)

window.mainloop()