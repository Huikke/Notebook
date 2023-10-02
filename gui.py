from tkinter import *

# Create the Tkinter application window
root = Tk()
root.title("Notebook")

# Handles saving to file
def save_to_file():
    with open(f"notes/{title.get()}.md", "w") as note:
        note.write(container.get("1.0", "end-1c"))

# Create title
title = Entry(root, width=50, borderwidth=3)
title.grid(row=1)

# Create container
container = Text(root, height=10, width=50, borderwidth=3)
container.grid(row=2)

# Create save button
button = Button(root, text="Save", command=save_to_file)
button.grid(row=3)

# Keeps application looping
root.mainloop()