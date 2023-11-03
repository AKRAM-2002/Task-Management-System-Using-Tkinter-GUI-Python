from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


### Test Login function
def login():
    username = user.get()
    password = pwd.get()

    if username == 'admin' and password == '123':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")


        Label(screen, text='Hello Everyone', bg ="#fff", font=('Calibiri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()


    elif username != 'admin' and password != '123':
        messagebox.showerror("Invalid","Invalid Username and Password")


    elif password != '123':
        messagebox.showerror("Invalid","Invalid Password")


    elif username != 'admin':
        messagebox.showerror("Invalid","Invalid Username")





#img = PhotoImage(file='Task-Management-System-Using-Tkinter-GUI-Python/assets/login1.png')

image = Image.open("Task-Management-System-Using-Tkinter-GUI-Python/assets/login1.png")

# Resize the image using resize() method
resize_image = image.resize((450, 400))
 
img = ImageTk.PhotoImage(resize_image)

Label(root, image=img, bg = 'white').place(x=420, y=70)

frame = Frame(root, width= 400, height=350, bg ='#fff')
frame.place(x =20, y =100)
heading = Label(frame, text="Login to your account", fg="#733702", bg="#0D0D0D", font=('Helvetica', 23, 'bold'))
heading.place(x = 20,y=5)


####################### Username Field

def on_enter(e):
    field = user.get()
    if field == 'Username':
        user.delete(0, 'end')
def on_leave(e):
    field = user.get()
    if field== '' :
        user.insert(0,'Username')
user = Entry(frame, width=25, fg='black', border=0, bg='white',font=('Helvetica', 11) )
user.place(x = 60, y= 80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x = 25, y = 107)

######################## Password Field
def on_enter(e):
    field = pwd.get()
    if field == 'Password':
        pwd.delete(0, 'end')
def on_leave(e):
    field = pwd.get()
    if field== '':
        pwd.insert(0,'Password')

pwd = Entry(frame, width=25, fg='black', border=0, bg='white',font=('Helvetica', 11) )
pwd.place(x = 60, y= 150)
pwd.insert(0, 'Password')
pwd.bind('<FocusIn>', on_enter)
pwd.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x = 25, y = 177)

#####################################################################

Button(frame, width= 39, pady=7, text='Sign in', bg='#0D0D0D', fg='#F28705', command=login , border=0).place(x=35, y = 204)
label = Label(frame, text="Don't have an account?", fg='black', bg="white", font=('Helvetica', 9)).place(x= 100, y =280)

register = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#733702',  )
register.place(x=230, y=280)







root.mainloop()