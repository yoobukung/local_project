from tkinter import *
from tkinter import ttk
import sqlite3
from collections import Counter

root = Tk()
root.title('mini customer relation management app')
root.geometry("1200x500")


# Database
connect = sqlite3.connect('tree_crm.db')
conn = connect.cursor()
conn.execute("""CREATE TABLE if not exists customers (
    first_name text,
    last_name text,
    id integer,
    address text,
    city text,
    state text,
    zipcode text,
    tel text
)""")


def query_database():
    connect = sqlite3.connect('tree_crm.db')
    conn = connect.cursor()
    conn.execute(""" SELECT rowid,  * FROM customers""")
    records = conn.fetchall()

    print(len(records[0]))

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent="", index="end", iid=count, text="", value=(
                record[1], record[2], record[3], record[4],
                record[5], record[6], record[7], record[8],),  tags=('evenrow'))
        else:
            my_tree.insert(parent="", index="end", iid=count, text="", value=(
                record[1], record[2], record[3], record[4],
                record[5], record[6], record[7], record[8],),  tags=('oddrow'))
        count += 1

    connect.close()


style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
                )
style.map('Treeview', background=[('selected', '#347083')])


# Frame
tree_frame = Frame(root)
tree_frame.pack(pady=15)

# Scroll

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree_scrollX = Scrollbar(tree_frame, orient='horizontal')
tree_scrollX.pack(side=BOTTOM, fill=X)

my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scrollX.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)
tree_scrollX.config(command=my_tree.xview)

# Column
my_tree['columns'] = ("First Name", "Last Name",
                      "ID", "Address", "City", "State",
                      "Zipcode", "Tel")

my_tree.column('#0', width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column('Last Name', anchor=W, width=140)
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Address', anchor=CENTER, width=140)
my_tree.column('City', anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column('Zipcode', anchor=CENTER, width=100)
my_tree.column('Tel', anchor=CENTER, width=140)

my_tree.heading('#0', text="", anchor=CENTER)
my_tree.heading('First Name', text='First Name', anchor=CENTER)
my_tree.heading('Last Name', text='Last Name', anchor=CENTER)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Address', text='Address', anchor=CENTER)
my_tree.heading('City', text='City', anchor=CENTER)
my_tree.heading('State', text='State', anchor=CENTER)
my_tree.heading('Zipcode', text='Zipcode', anchor=CENTER)
my_tree.heading('Tel', text="Tel", anchor=CENTER)


my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# Data Frame
data_frame = LabelFrame(root, text="Records")
data_frame.pack(fill="x", expand="yes", padx=50,)

fn_label = Label(data_frame, text="First Name",)
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text='Last Name',)
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text='ID',)
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

addr_label = Label(data_frame, text='Address',)
addr_label.grid(row=1, column=0, padx=10, pady=10)
addr_entry = Entry(data_frame)
addr_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text='City',)
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="State",)
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zip_label = Label(data_frame, text='Zipcode',)
zip_label.grid(row=1, column=6, padx=10, pady=10)
zip_entry = Entry(data_frame)
zip_entry.grid(row=1, column=7, padx=10, pady=10)

tel_label = Label(data_frame, text="Tel",)
tel_label.grid(row=1, column=8, padx=10, pady=10)
tel_entry = Entry(data_frame)
tel_entry.grid(row=1, column=9, padx=10, pady=10)

# function


def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def clear_entrise():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    addr_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    tel_entry.delete(0, END)


def select_record(e):
    # Clear Entry Box
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    addr_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    tel_entry.delete(0, END)

    # Grab Record Number
    selected = my_tree.focus()
    # Grab Record
    values = my_tree.item(selected, 'values')

    # Output to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    addr_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zip_entry.insert(0, values[6])
    tel_entry.insert(0, values[7])


def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(
        fn_entry.get(),
        ln_entry.get(),
        id_entry.get(),
        addr_entry.get(),
        city_entry.get(),
        state_entry.get(),
        zip_entry.get(),
        tel_entry.get(),
    ))
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    addr_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)
    tel_entry.delete(0, END)


# Button
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=50)

update_button = Button(
    button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_all_button = Button(
    button_frame, text="Remove all Record", command=remove_all)
remove_all_button.grid(row=0, column=4, padx=10, pady=10)

remove_one_button = Button(
    button_frame, text="Remove one Record", command=remove_one)
remove_one_button.grid(row=0, column=6, padx=10, pady=10)

remove_many_button = Button(
    button_frame, text="Remove many Record", command=remove_many)
remove_many_button.grid(row=0, column=8, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move up", command=up)
move_up_button.grid(row=0, column=10, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move down", command=down)
move_down_button.grid(row=0, column=11, padx=10, pady=10)

select_button = Button(
    button_frame, text="Clear Entry boxes", command=clear_entrise)
select_button.grid(row=0, column=12, padx=10, pady=10)

export_button = Button(button_frame, text="Export CSV")
export_button.grid(row=0, column=13, padx=10, pady=10)

import_button = Button(button_frame, text="Import Sheet")
import_button.grid(row=0, column=14, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

query_database()

root.mainloop()


# Add dummies
# for record in data:
#     conn.execute("""INSERT INTO customers VALUES (
#         :first_name, :last_name, :id, :address, :city, :state, :zipcode, :tel
# )""", {
#         'first_name': record[0],
#         'last_name': record[1],
#         'id': record[2],
#         'address': record[3],
#         'city': record[4],
#         'state': record[5],
#         'zipcode': record[6],
#         'tel': record[7]

#     }
#     )
# connect.commit()
# connect.close()


# Fake Data
# data = [
#     ["Python", "pt", 1, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Javascript", "jv", 2, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Java", "jv", 3, "4454 Rad-U-tid Rd.", "Bangkok",
#         "Minburi", "10510", "099 045 0202"],
#     ["Nodejs", "js", 4, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Djnago", "dj", 5, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Python", "pt", 6, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Python", "pt", 7, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Python", "pt", 8, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Python", "pt", 9, "4454 Rad-U-tid Rd.",
#         "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Djnago", "dj", 5, "4454 Rad-U-tid Rd.",
#      "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Djnago", "dj", 5, "4454 Rad-U-tid Rd.",
#      "Bangkok", "Minburi", "10510", "099 045 0202"],
#     ["Djnago", "dj", 5, "4454 Rad-U-tid Rd.",
#      "Bangkok", "Minburi", "10510", "099 045 0202"],
# ]
