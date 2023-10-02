from tkinter import *
import main

# Create the Tkinter application window
root = Tk()
root.title("Notebook")

# Create an entry for input name of a file
name = Entry(root, width=50, borderwidth=3)
name.grid(row=1)

# Create a textbox to write text into
content = Text(root, height=10, width=50, borderwidth=3)
content.grid(row=2)

# Create save button
button = Button(root, text="Save", command=lambda: main.save_note(name.get(), content.get("1.0", "end-1c")))
button.grid(row=3)

# Keeps application looping
root.mainloop()