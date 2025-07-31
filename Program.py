from tkinter import *

from tkinter.filedialog import askopenfilename

window = Tk()

window.title("Text Editor")

window.geometry("600x500")

window.rowconfigure(0,minsize = 800,weight = 1)

window.columnconfigure(0,minsize = 800,weight = 1)

def open_file():
    
    """Open a file for editing"""
        
    filepath = askopenfilename(
        
        filetypes = [("Text files", "*txt"), ("All files", "*.*")]
        
    )
    
    if not filepath:
        
        return
    
    txt_edit.delete(1.0, END) #Clear the text area
    
    with open(filepath, "r") as input_file:
        
        text = input_file.read()
        
        txt_edit.insert(END, text)
        
        input_file.close()
        
        window.title(f"Text Editor - {filepath}")\
            
def save_file():
    
    """Save the current text to a file"""
    
    filepath = askopenfilename(
        
    defaultextension = ".txt",
    
    filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
    
    )
        
    if not filepath:
        
        return
    
    with open(filepath, "w") as output_file: