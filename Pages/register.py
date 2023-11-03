from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk

import os  # Import the os module

# Get the path to the project's root directory
project_root = os.path.dirname(__file__)

# Define the path to the 'Database' folder
database_folder = os.path.join(project_root, 'Database')

# Create the 'Database' folder if it doesn't exist
if not os.path.exists(database_folder):
    os.makedirs(database_folder)

window = Tk()
window.title("Register")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)


### Test Register function

def register():
    username = user.get()
    password1 = pwd.get()
    password2 = pwd_confirm.get()

    if password1 == password2:
        try:
            # Specify the path to 'data.txt' in the 'Database' folder
            data_file_path = os.path.join(database_folder, 'data.txt')

            file = open(data_file_path, 'r+')
            d = file.read()
            r = ast.literal_eval(d)  # Assign the parsed dictionary to 'r'

            dict2 = {username: password1}  # Use 'username' and 'password1'
            r.update(dict2)

            file.truncate(0)
            file.close()

            file = open(data_file_path, 'w')
            w = file.write(str(r))

            messagebox.showinfo('Signup', "You signed up successfully")
        except:
            # Specify the path to 'data.txt' in the 'Database' folder
            data_file_path = os.path.join(database_folder, 'data.txt')

            file = open(data_file_path, 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', 'Both Passwords should match')


image = Image.open("Task-Management-System-Using-Tkinter-GUI-Python/assets/register.png")

# Resize the image using resize() method
resize_image = image.resize((450, 400))
 
img = ImageTk.PhotoImage(resize_image)

Label(window, image=img, bg = 'white').place(x=420, y=70)

frame = Frame(window, width= 400, height=350, bg ='#fff')
frame.place(x =20, y =50)
heading = Label(frame, text="Create new account", fg="#733702", bg="#0D0D0D", font=('Helvetica', 23, 'bold'))
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


######################## Confirm Password Field
def on_enter(e):
    field = pwd_confirm.get()
    if field == 'Confirm Password':
        pwd_confirm.delete(0, 'end')
def on_leave(e):
    field = pwd_confirm.get()
    if field== '':
        pwd_confirm.insert(0,'Confirm Password')

pwd_confirm = Entry(frame, width=25, fg='black', border=0, bg='white',font=('Helvetica', 11) )
pwd_confirm.place(x = 60, y= 210)
pwd_confirm.insert(0, 'Confirm Password')
pwd_confirm.bind('<FocusIn>', on_enter)
pwd_confirm.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x = 25, y = 237)

#####################################################################

Button(frame, width= 39, pady=7, text='Sign in', bg='#0D0D0D', fg='#F28705', border=0, command=register).place(x=35, y = 290)
label = Label(frame, text="Already a Member?", fg='black', bg="white", font=('Helvetica', 9)).place(x= 100, y =330)

login = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#733702',  )
login.place(x=210, y=330)



window.mainloop()