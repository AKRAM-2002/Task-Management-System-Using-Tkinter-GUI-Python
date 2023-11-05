from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import ast
import os  # Import the os module

# Get the path to the project's root directory
project_root = os.path.dirname(__file__)

# Define the path to the 'Database' folder
database_folder = os.path.join(project_root, 'Database')

# Create the 'Database' folder if it doesn't exist
if not os.path.exists(database_folder):
    os.makedirs(database_folder)

root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


#============================Login function=================

def login():
    username = user.get()
    password = pwd.get()


    data_file_path = os.path.join(database_folder, 'data.txt')

    file = open(data_file_path, 'r+')
    d = file.read()
    r = ast.literal_eval(d)  # Assign the parsed dictionary to 'r'

    file.close()

    # print(r.keys())
    # print(r.values())


    if username in r.keys() and password in r.values():
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")


        Label(screen, text='Hello Everyone', bg ="#fff", font=('Calibiri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'Invalid userame or password')
###################################################################################

def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#F27507')
    win.resizable(False, False)

    # ====== Username ====================
    username = Entry(win, bg="white", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=0)
    username.place(x=40, y=80, width=256, height=50)
    username.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    username_label = Label(win, text='• Username', fg="#FFFFFF", bg='#0D0D0D',
                         font=("yu gothic ui", 11, 'bold'))
    username_label.place(x=40, y=50)

    # ====  New Password ==================
    new_password_entry = Entry(win, bg="white", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=0)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#0D0D0D',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=150)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#F28705', text='Update Password', bg='#0D0D0D', 
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#733702")
    update_pass.place(x=40, y=260, width=256, height=45)
   

#=====================================================================
#============================SIGN UP PAGE Starts here=================
#=====================================================================

def signup_command():
    window = Toplevel(root)
    
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

                
                messagebox.showinfo('Signup', "You signed up successfully!")
                
            except:
                # Specify the path to 'data.txt' in the 'Database' folder
                data_file_path = os.path.join(database_folder, 'data.txt')

                file = open(data_file_path, 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()
            
        else:
            messagebox.showerror('Invalid', 'Both Passwords should match')


    def sign():
        window.destroy()


    


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
    user = Entry(frame, width=25, fg='black', border=0, bg='white',font=("yu gothic ui semibold", 12), highlightthickness=1 )
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

    pwd = Entry(frame, width=25, fg='black', border=0, bg='white',font=("yu gothic ui semibold", 12), highlightthickness=1 )
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

    pwd_confirm = Entry(frame, width=25, fg='black', border=0, bg='white',font=("yu gothic ui semibold", 12), highlightthickness=1 )
    pwd_confirm.place(x = 60, y= 210)
    pwd_confirm.insert(0, 'Confirm Password')
    pwd_confirm.bind('<FocusIn>', on_enter)
    pwd_confirm.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x = 25, y = 237)

    #####################################################################

    Button(frame, width= 39, pady=7, text='Sign up', bg='#0D0D0D', fg='#F28705', border=0, command=register).place(x=35, y = 290)
    label = Label(frame, text="Already a Member?", fg='black', bg="white", font=('Helvetica', 9)).place(x= 100, y =330)

    login = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#733702', command=sign )
    login.place(x=210, y=330)



    window.mainloop()


#=====================================================================
#============================SIGN UP PAGE FINISH HERE=========================================
#=====================================================================




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
user = Entry(frame, width=25, fg='black', border=0, bg='white',font=("yu gothic ui semibold", 12), highlightthickness=1)
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

pwd = Entry(frame, width=25, fg='black', border=0, bg='white',font=("yu gothic ui semibold", 12), highlightthickness=1 )
pwd.place(x = 60, y= 150)
pwd.insert(0, 'Password')
pwd.bind('<FocusIn>', on_enter)
pwd.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x = 25, y = 177)

#####################################################################

forget_pwd = Button(frame, width=36, text='Forget Password?', border=0, bg='white', cursor='hand2', fg='#733702', command=forgot_password)
forget_pwd.place(x=140, y=220)

Button(frame, width= 39, pady=7, text='Sign in', bg='#0D0D0D', fg='#F28705', command=login , border=0).place(x=35, y = 244)
label = Label(frame, text="Don't have an account?", fg='black', bg="white", font=('Helvetica', 9)).place(x= 100, y =300)


register = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#733702',command=signup_command)
register.place(x=230, y=300)




root.mainloop()