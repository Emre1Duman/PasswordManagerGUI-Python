from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [(random.choice(letters)) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, string=f"{password}") #Populates the password text box with the new generated password
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    #Getting the text entered by user and assigning to variables
    new_website = website_entry.get()
    new_username = username_entry.get()
    new_password = password_entry.get()
    new_data = {
        new_website: {
            "email" : new_username,
            "password" : new_password,
        }
    }

    if len(new_website) == 0 or len(new_password) == 0: #Checks to if the fields are left empty
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        with open("data.json", "r") as data_file:
            #Readng old data
            data = json.load(data_file)
            #Updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, 'end') #Clears field
        password_entry.delete(0, 'end')


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
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()