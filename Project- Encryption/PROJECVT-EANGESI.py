from tkinter import *

root = Tk()

root.title("CHICKIN")

root.geometry("400x400")


unput = Entry(root)

unput.place(relx=0.5, rely=0.4, anchor=CENTER)

Lobel = Label(root, text="Name is Ascii")

Ladel = Label(root, text="Encryptedddd txt")

Lobel.place(relx=0.5, rely=0.6, anchor=CENTER)
Ladel.place(relx=0.5, rely=0.7, anchor=CENTER)

def asciichickin():
    text = unput.get()
    for letter in text:
        Lobel["text"] += str(ord(letter))
        ascii=int(ord(letter))
        Encrypt=ascii-1
        Ladel["text"] += str(chr(Encrypt))

button= Button(root, command=asciichickin, text="TRANSFOR")
button.place(relx=0.5, rely=0.3, anchor=CENTER)
root.mainloop()