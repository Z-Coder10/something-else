#Information
from tkinter import *

root = Tk()

root.geometry("400x300")

root.title("Main Window")

def topWin():
    
    top = Toplevel()
    
    top.geometry('180x100')
    
    top.title("Top level window")
    
    l2 = Label(top,text = "This is the top level window")
    
    l2.pack()
    
l = Label(root,text = "This is the root window")

btn = Button(root,text = 'Click here to open another window' ,command=topWin)

l.pack()

btn.pack()

root.mainloop()

