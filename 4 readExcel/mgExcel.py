from tkinter import *
import pandas as pd  # already pip install pandas numpy openpyxl
from tkinter import ttk, filedialog

# App name

root = Tk()
root.title("mgExcel App")
root.geometry("750x550")

my_frame = Frame(root)
my_frame.pack(pady=20)


# Treeview
my_tree = ttk.Treeview(my_frame)
Scrollbar


# Function
def file_open():

    filename = filedialog.askopenfilename(
        initialdir="C:/",
        title="Open A File Sheet",
        filetype=(("xlsx files", "*.xlsx"), ("All file", "*,*"))
    )
    df = pd.read_excel(filename).fillna('')

    if filename:
        try:
            filename = r"{}".format(filename)

        except ValueError:
            my_label.config(
                text="File couldn't be opened ... try again! \nPleas, Check something wrong")
        except FileNotFoundError:
            my_label.config(text="File couldn't be found ")
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"

    # Headers
    for column in my_tree["column"]:
        my_tree.heading(column, text="column")

    # put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)

    # Pack the treeview finally
    my_tree.pack()


def clear_tree():
    my_tree.delete(*my_tree.get_children())


# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
