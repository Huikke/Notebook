# Simple notetaking tool
import os

# Create a new note to notes folder
def create_note():
    title = input("Note title: ")
    print("Note content: ")
    with open(f"notes/{title}.md", "w") as note:
        first = True
        while True:
            line = input()
            if line == "":
                break
            if first != True:
                note.write("\n")
            note.write(line)
            first = False

# Read a note in notes folder
def view_note():
    title = input("Note title: ")
    try:
        with open(f"notes/{title}.md", "r") as note:
            print(f"{title} content:")
            print(note.read())
    except FileNotFoundError:
        print("No existing notes")

# List all notes in notes folder
def list_notes():
    notes = []
    files = os.listdir("notes")

    for file in files:
        if file[-3:] == ".md":
            notes.append(file)

    print("Notes:")
    for note in notes:
        print(f"- {note}")

# Print UI
def ui():
    print("Choose action:")
    print("1. Create a new note")
    print("2. View a note")
    # print("3. Delete a note")
    print("4. Show notes")
    print("0. End program")

# Application main loop
while True:
    ui()
    choice = input("Choice: ")
    if choice == "1":
        create_note()
    elif choice == "2":
        view_note()
    elif choice == "4":
        list_notes()
    elif choice == "0":
        break
    else:
        print("Invalid Input!")
    print()