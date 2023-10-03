from tkinter import *
import main

# Create the Tkinter application window
root = Tk()
root.title("Notebook")

# Handle updating note view when clicking on listbox
def open_note(event):
    note_name = listbox.get(ANCHOR)
    note_content = main.view_note(note_name)
    name.delete(0, END)
    content.delete("1.0", END)
    name.insert(0, note_name)
    content.insert("1.0", note_content)

def save_note():
    main.save_to_file(name.get(), content.get("1.0", "end-1c"))
    listbox_update()

def listbox_update():
    listbox.delete(0, END)
    note_names = main.note_names()
    for note_name in note_names:
        listbox.insert(END, note_name)

# Create an entry for input name of a file
name = Entry(root, width=50, borderwidth=3)
name.grid(row=1, column=1)

# Create a textbox to write text into
content = Text(root, height=10, width=50, borderwidth=3)
content.grid(row=2, column=1)

# Listbox to choose notes
listbox = Listbox(root)
listbox.grid(row=2, column=0)
listbox_update()
listbox.bind("<<ListboxSelect>>", open_note)

# Create save button
button = Button(root, text="Save", command=save_note)
button.grid(row=3, column=1)

# Keeps application looping
root.mainloop()