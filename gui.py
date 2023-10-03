from tkinter import *
from tkinter import messagebox
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

# Removes name and content, simulating creating a new page
def clear_page():
    name.delete(0, END)
    content.delete("1.0", END)

# Save note to local file system
def save_note():
    # Don't do anything, when name is empty
    if name.get() == "":
        return
    
    main.save_to_file(name.get(), content.get("1.0", "end-1c"))
    listbox_update()

# Delete note from local file system after a confirmation
def delete_note():
    # Don't do anything, when name is empty
    if name.get() == "":
        return

    # Ask user whether for confirmation using messagebox popup
    response = messagebox.askokcancel("Notebook", f"Do you want to delete the note '{name.get()}'?", icon='warning')
    if response == True:
        main.delete_file(name.get())

    # Update listbox and clear page after deletion
    listbox_update()
    clear_page()

# Updates listbox view
def listbox_update():
    listbox.delete(0, END)
    note_names = main.note_names()
    for note_name in note_names:
        listbox.insert(END, note_name)

title = Label(root, text="The Notebook").grid(row=1, column=0)

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

# Create new button (which really just deletes containers)
new_button = Button(root, text="New", command=clear_page)
new_button.grid(row=3, column=0)

# Create save button
save_button = Button(root, text="Save", command=save_note)
save_button.grid(row=3, column=1)

# Create delete button
delete_button = Button(root, text="Delete", command=delete_note)
delete_button.grid(row=4, column=0)

# Keeps application looping
root.mainloop()