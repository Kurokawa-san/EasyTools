import webbrowser
import time
from tkinter import *
import tkinter.messagebox

window = Tk()

def script() :
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
    time.sleep(3)
    tkinter.messagebox.showinfo("LMAO", "YOU GOT RICKROLLED!!!!! \n-ALDRICH JUSTIN LOTAS \ni put alot of effort to rick roll you all \np.s don't tell the others :)")
    window.destroy()

    
    
lbl=Label(window, text="CLICK THE BUTTON", fg='green', font=("Comic Sans", 16))
lbl.place(x=60, y=50)
btn=Button(window, text="Run EasyTools", fg='red', command = script)
btn.place(x=100, y=100)
window.title('EASYTOOLS GUI')
window.geometry("300x200+500+250")
window.mainloop()