from tkinter import *
from tkinter import messagebox
window = Tk()

# window Creation
window.title("Password Manager")
window.config(padx=50,pady=20,bg="black")

# Canvas Creation
canvas = Canvas(width=400,height=400,bg="black",highlightthickness=0)
passimage = PhotoImage(file="passimage.png")
display = canvas.create_image(200,200,image = passimage)
canvas.grid(row=0,column=1)

# Label Creation
web_label = Label(text="Website:",bg="black",font=("times new roman",24,"normal"))
web_label.grid(row=1,column=0)

# website entry 
web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()


# email/username label
elabel = Label(text="Email/Username:",bg="black",font=("times new roman",24,"normal"))
elabel.grid(row=2,column=0)

# Email/Username Entry
emailentry = Entry(width=35)
emailentry.grid(row=2,column=1,columnspan=2)
emailentry.insert(0,"lakshay@gmail.com")

# Password Label 
pass_label = Label(text="Password:",bg="black",font=("times new roman",24,"normal"))
pass_label.grid(row=3,column=0)

# Password Entry
pass_entry = Entry(width=20)
pass_entry.grid(row=3,column=1)

# Generate Passwod Button
generate_button = Button(text="Generate Password")
generate_button.grid(row=3,column=2)


def save():
    website = web_entry.get()
    email = emailentry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR !!" ,message=" Do not leave any Fields empty !😤")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",message=f"The Details You Entered :\nwebsite ={website}\nEmail = {email}\nPassword = {password}\nIs It OK to Save ??")
        if is_ok:
            with open("password.txt","a") as datafile:
                datafile.write(f"{website} | {email} | {password} \n")
                web_entry.delete(0,END)
                pass_entry.delete(0,END)



# add Button
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)









window.mainloop()