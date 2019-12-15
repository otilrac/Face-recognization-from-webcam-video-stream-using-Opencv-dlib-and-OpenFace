from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter.font import Font
import os
import os.path
root  = Tk()

def login():
    stri1="kaushik"
    stri2="bolt1234"
    username = entry1.get()
    password = entry2.get()
    label0=Label(root, text="sucessful Login",bg="black",fg="green")
    label1=Label(root, text="Incorrect username or password", bg="black", fg="yellow")
    if(stri1==username and stri2==password):
        

        
        label0.place(x=1035,y=650)

        os.system("python dlib_image.py")


    else:

        
        label1.place(x=1035,y=650)
    
        

class PageOne(tk.Frame):
    images = []

    def __init__(self, parent, controller):
        super(PageOne,self).__init__(parent,bg=Gray_Back_Page_1)


photo=PhotoImage(file="C:\\Users\\Bharath\\Desktop\\boltzeye\\Artboard 1.png")
PageOne.images.append(photo) 
l=Label(root,image=photo)
l.image=photo
l.grid()

my_font=Font(family='Times New Roman',size=12,weight='bold')
my_fontD=Font(family='Product Sans',size=12,weight='bold')
theLabel1 = Label(root, text="  USERNAME  ",bg="black", fg="purple",font=("Forte",13))
theLabel1.place(x=1000,y=500)





theLabel2 = Label(root, text="  PASSWORD  ",bg="black", fg="purple",font=("Forte",13))
theLabel2.place(x=1000,y=540)




entry1=Entry(root)
entry1.place(x=1122,y=502)



entry2=Entry(root,show="*")
entry2.place(x=1122,y=542)



c=Checkbutton(root,text="  keep me logged in",bg="black",fg="white")
c.place(x=1060,y=570)



button1=Button(root,text="  Log In  ", bg="blue",fg="white",command=login,font=("Harrington",12,"bold"))
button1.place(x=1010 ,y=610)
root.mainloop()


