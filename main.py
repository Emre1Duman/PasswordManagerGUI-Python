from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_website = website_entry.get()
    new_username = username_entry.get()
    new_password = password_entry.get()
    f = open("data.txt", "a")
    f.write(f"\n{new_website}| {new_username} | {new_password}")
    website_entry.delete(0, 'end') #Clears field
    password_entry.delete(0, 'end')
    f.close()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(122, 90, image=img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = Entry(width=35)
username_entry.insert(END, string="uzumaki@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)


#Buttons
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()





