#Opening Staments
from tkinter import *

window = Tk()

window.title("Event Handler")

window.geometry("100x100")

def handle_keypress(event):
    
    """Print the character associated to the key pressed"""
    
    ("You pressed:", event.char)
    
    #Bind keypress event handler keypress
    
    window.bind("<KeyPress>",handle_keypress)
    
def handle_click(event):
    
    """Print the coordinates of the mouse click"""
    
    print("Mouse clicked at:", event.x, event.y)
        
button = Button (text = "   Click Me")
        
button.pack()
        
        #Bind click event handler click
        
button.bind("<Button-1>", handle_click)
        
        
        
window.mainloop()