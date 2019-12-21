

from tkinter import *
from tkinter import messagebox

from db import Database 

db = Database('phone_book.db')

### ------ Backend / Functionality ------ ### 


def populate_list():
    contacts_list.delete(0, END)
    for row in db.fetch():
        contacts_list.insert(END, row)

def add_contact():

	if first_name_text.get() == '' or last_name_text.get() == '' or phone_number_text.get() == '':
		messagebox.showerror('Error Message', 'Please include ALL fields' )
		return
	db.insert(first_name_text.get(), last_name_text.get(), phone_number_text.get())
	contacts_list.delete(0, END)
	contacts_list.insert(END, (first_name_text.get(), last_name_text.get(), phone_number_text.get()))

	clear_text()
	populate_list()


def select_contact(event):
    try:
        global selected_contact
        index = contacts_list.curselection()[0]
        selected_contact = contacts_list.get(index)

        first_name_entry.delete(0, END)
        first_name_entry.insert(END, selected_contact[1])
        last_name_entry.delete(0, END)
        last_name_entry.insert(END, selected_contact[2])
        phone_number_entry.delete(0, END)
        phone_number_entry.insert(END, selected_contact[3])

    except IndexError:
        pass
	 

def delete_contact():
	db.delete(selected_contact[0])
	clear_text()
	populate_list() 


def update_contact():
	db.update(selected_contact[0], first_name_text.get(), last_name_text.get(),
              phone_number_text.get())
	populate_list()


def clear_text():
	first_name_entry.delete(0, END)
	last_name_entry.delete(0, END) 
	phone_number_entry.delete(0, END)  



### ------ Frontend / User Interface    ------ ### 

phone_book = Tk()

## First Name 

first_name_text = StringVar()
first_name_label = Label(phone_book ,text="First Name:", font=('bold', 15), pady=20, padx=20)
first_name_label.grid(row=1, column=0, sticky=W)
first_name_entry = Entry(phone_book, textvariable= first_name_text, border=4)
first_name_entry.grid(row=1, column=1, pady=0, padx=0)


## Last Name

last_name_text = StringVar()
last_name_label = Label(phone_book ,text="Last Name:", font=('bold', 15), pady=20, padx=20)
last_name_label.grid(row=2, column=0, sticky=W)
last_name_entry = Entry(phone_book, textvariable= last_name_text, border=4)
last_name_entry.grid(row=2, column=1, pady=0, padx=0)


## Phone number

phone_number_text = StringVar()
phone_number_label = Label(phone_book ,text="Phone Number:", font=('bold', 15), pady=20, padx=20)
phone_number_label.grid(row=3, column=0, sticky=W)
phone_number_entry = Entry(phone_book, textvariable= phone_number_text, border=4)
phone_number_entry.grid(row=3, column=1, pady=0, padx=0)


## Buttons

add_btn = Button(phone_book, text='Add Contact', width=12, bg='green', command=add_contact, border=4)
add_btn.grid(row=4, column=0, pady=40, padx=20)

delete_btn = Button(phone_book, text='Delete Contact', width=12, bg='red', command=delete_contact)
delete_btn.grid(row=4, column=1, pady=40, padx=20)

update_btn = Button(phone_book, text='Update Contact', width=12, bg='yellow', command=update_contact)
update_btn.grid(row=4, column=2, pady=40, padx=20)

clear_btn = Button(phone_book, text=' xX Clear text Xx', width=12, bg='grey', command=clear_text)
clear_btn.grid(row=4, column=3, pady=40, padx=20)


## Contacts list 
contacts_list = Listbox(phone_book, height=10, width=36, border=1)
contacts_list.grid(row=1, column=3, columnspan=3, rowspan=3, pady=10, padx=0)


# Create scrollbar
scrollbar = Scrollbar(phone_book)
scrollbar.grid(row=2, column=6)

 
# Set scroll to listbox
contacts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=contacts_list.yview)


# Bind select
contacts_list.bind('<<ListboxSelect>>', select_contact)



### ------ Run main programme  ------ ### 

phone_book.geometry("850x300")
phone_book.title("Phone Book")

populate_list()

phone_book.mainloop()


