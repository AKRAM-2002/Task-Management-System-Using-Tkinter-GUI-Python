from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import os

root = Tk()
#image = PhotoImage(file='Task-Management-System-Using-Tkinter-GUI-Python/assets/man.png')
image = Image.open("Task-Management-System-Using-Tkinter-GUI-Python/assets/man2.png")
# Resize the image using resize() method
resize_image = image.resize((390, 350))
    
img = ImageTk.PhotoImage(resize_image)



root.geometry('925x500+300+200')
root.config(background= '#F28705')


welcome_label = Label(text = "YOUR FAVOURITE TASK MANAGER SYSTEM", bg ="#F28705", font= ("Trebuchet Ms", 15, "bold"), fg="#FFFFFF")
welcome_label.place(x = 270, y = 25)


bg_label = Label(root, image=img, bg="#F28705")
bg_label.place(x = 280, y= 65)


progress_label = Label(root, text="Loading...",  font= ("Trebuchet Ms", 13, "bold"), fg="white", bg="#F28705")
progress_label.place(x = 400, y= 440)


progress = ttk.Style()
progress.theme_use('clam')
progress.configure('red.Horizontal.TProgressbar', background="#733702")


progress = Progressbar(root, orient=HORIZONTAL, length= 400, mode='determinate', style= "red.Horizontal.TProgressbar")
progress.place(x = 260 , y = 410)


def top():
    root.withdraw()
    os.system("Mainlogin.py")
    root.destroy()

i = 0
def load():
    global i
    if i <= 10:
        txt = 'Loading... ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

load()
root.resizable(False, False)
root.mainloop()

