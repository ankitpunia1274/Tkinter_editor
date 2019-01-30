from tkinter import Tk,Menu,filedialog
#import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext as ScrolledText
root=Tk(className="AEditor")
textArea=ScrolledText.ScrolledText(root,width=800,height=600)
textArea.pack()
#textArea.pack()
def openfile():
    file=filedialog.askopenfile(parent=root,mode='rb',title="select file",filetype=(("Text file","*.txt"),("All files","*_*")))
                                
    if(file!=None):
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()
def savefile():
    file=filedialog.asksaveasfile(mode='w')
    if(file!=None):
        data=self.textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
def help():
    print("This is Editor to save file and save important data of computer user this if of VERSION 2.0,THANKS FOR USING THIS FOR MORE HELP:www.google.coms")
def exit():
    print("Thanks For Using This Editor")
    answer=tkinter.messagebox.askokcancel("are you sure?","are you sure.....your data will lost")
    if(answer):
        root.destroy()
def smallwindow():
    #root.minsize(width=200,height=300)
    root.geometry("300x300")
def resetsize():
    #root.minsize(width=200,height=300)
    root.geometry("800x600")

root.geometry("800x600")
menu1=Menu(root)
root.config(menu=menu1)
submenu=Menu(menu1)
##first Menu bar
menu1.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New           Ctrl+N")
submenu.add_command(label="Open...       Ctrl+O",command=openfile)
submenu.add_command(label="Save          Ctrl+S",command=savefile)
submenu.add_command(label="Save As ")
submenu.add_separator()
submenu.add_command(label="Exit",command=exit)
##second menu bar
submenu1=Menu(menu1)
menu1.add_cascade(label="Edit",menu=submenu1)
submenu1.add_command(label="Resize The Editor Window",command=smallwindow)
submenu1.add_command(label="Reset The Size",command=resetsize)
submenu1.add_command(label="Cut         Ctrl+X")
submenu1.add_command(label="Cut         Ctrl+X")
submenu1.add_command(label="Copy        Ctrl+V")
submenu1.add_command(label="Paste       Ctrl+N")
submenu1.add_command(label="Select All  Ctrl+A")
submenu1.add_command(label="Exit",command=exit)
##Third menu bar
submenu2=Menu(menu1)
menu1.add_cascade(label="Format",menu=submenu2)
submenu2.add_command(label="Word Wrap")
submenu2.add_command(label="Font")
submenu2.add_command(label="Exit",command=exit)
##fourth menu bar
submenu3=Menu(menu1)
menu1.add_cascade(label="View",menu=submenu3)
submenu3.add_command(label="Status Bar")
submenu3.add_command(label="Exit",command=exit)
#fifth bar
submenu4=Menu(menu1)
menu1.add_cascade(label="Help",menu=submenu4)
submenu4.add_command(label="Editor Help",command=help)
submenu4.add_command(label="Exit",command=exit)

root.mainloop()





