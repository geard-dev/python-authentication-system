from tkinter import *

def access():
    print(username_login_info+" has logged in")
    # Code to run when user sucessfully logged in:
    

def register_user():

    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Sucessful", fg = "green" ,font = ("calibri", 11)).pack()
    print("User "+username_info+" has registered")

def login_user():

    global username_login_info
    username_login_info = username.get()
    password_login_info = password.get()

    file=open(username_login_info+".txt", "r")
    username_from_data = file.readline()
    password_from_data = file.readline()
    file.close()

    if password_login_info == password_from_data:
        Label(screen2, text = "Login Sucessful", fg = "green" ,font = ("calibri", 11)).pack()
        access()
    else:
        Label(screen2, text = "Incorrect Password", fg = "red" ,font = ("calibri", 11)).pack()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
  
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen2, text = "Please enter details below").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username * ").pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry =  Entry(screen2, textvariable = password)
    password_entry.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_user).pack()

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Authentication System by geard-dev")
  Label(text = "Authentication System by geard-dev", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()