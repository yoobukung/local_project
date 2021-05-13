from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator Program")
root.geometry("500x300")


def newrandom():
    # clear Entry Box
    pwEntry.delete(0, END)

    # Get PW Length and convert integer
    pwLength = int(myEntry.get())
    myPassword = ""

    for x in range(pwLength):
        myPassword += chr(randint(33, 126))

    # Output password to the screen
    pwEntry.insert(0, myPassword)


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pwEntry.get())


# GUI
lf = LabelFrame(root, text="How many Charctors?")
lf.pack(pady=20, padx=30)

myEntry = Entry(lf, font=("Helvetica", 18))
myEntry.pack(pady=20, padx=20)

pwEntry = Entry(root, text="", font=("Helvetica", 18),
                bd=0, bg="systembuttonface")
pwEntry.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)

# Button
myButton = Button(myFrame, text="Generate password", command=newrandom)
myButton.grid(row=0, column=0, padx=10)

clipButton = Button(myFrame, text="Copy to Clipboad", command=clipper)
clipButton.grid(row=0, column=1, padx=10)


root.mainloop()
