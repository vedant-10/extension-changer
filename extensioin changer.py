from cProfile import label
import os
from tkinter import*
import tkinter as tk
from tkinter.font import BOLD

window=tk.Tk()
window.geometry("450x250+580+250")
window.config(bg="#fff")
window.overrideredirect(True)

path_var=tk.StringVar()
exe_var=tk.StringVar()

def start():
    path=path_var.get()
    exe=exe_var.get()
    base=os.path.splitext(path)[0]
    os.rename(path,base+exe)
    l2.configure(text="Done.....")
    e1.delete(0,END)
    e2.delete(0,END)

l1=Label(window,font=("Sylfaen",15),fg='white',bg='#008080',justify=CENTER,width=40,text="Please place this file in the folder\n where your file is present.&\nEnter the file name only with proper extentions")
l1.place(anchor=CENTER,relx=0.5,rely=0.2)
l2=Label(window,fg='black',font=("Sylfaen",10,BOLD),bg='#fff')
l2.place(anchor=CENTER,relx=0.5,rely=0.97)

b1=Button(window,text="Start",width=10, command=start,font=('Sylfaen',14),bg='#57a1f8',fg='white',border=0,cursor='hand2')
b1.place(relx=0.6,rely=0.45)
b2=Button(window,text="Cancel",width=10,command=window.destroy,font=('Sylfaen',14),bg='#57a1f8',fg='white',border=0,cursor='hand2')
b2.place(relx=0.15,rely=0.45)

e1=Entry(window,width=20,border=0,textvariable=path_var,font=('Sylfaen',12))
e1.place(x=20,y=165)
Frame(window,width=170,height=2,bg='black').place(x=20,y=195)
Label(window,font=('Sylfaen',11),fg='black',bg='white',text="File name\t\t\t            Extension to change").place(x=20,y=200)
e2=Entry(window,width=20,border=0,textvariable=exe_var,font=('Sylfaen',12))
e2.place(x=230,y=165)
Frame(window,width=170,height=2,bg='black').place(x=230,y=195)

window.mainloop()