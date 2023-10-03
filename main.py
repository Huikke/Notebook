# Simple notetaking tool
import os

# Create a new note to notes folder (CLI only)
def create_note():
    name = input("Note name: ")
    # If a note with same name already exist, abort immedially
    if os.path.exists(f"notes/{name}.md"):
        print("Note with the same name already exist")
        return
    
    # Gives user ability to write multiple lines until they linebreak at an empty line
    print("Note content: ")
    with open(f"notes/{name}.md", "w") as note:
        first = True
        while True:
            line = input()
            if line == "":
                break
            if first != True:
                note.write("\n")
            note.write(line)
            first = False

# Handle creation and save to file (GUI only)
def save_note(name, content):
    with open(f"notes/{name}.md", "w") as note:
        note.write(content)

# Read a note in notes folder
def view_note(name):
    if os.path.exists(f"notes/{name}.md"):
        with open(f"notes/{name}.md", "r") as note:
            return note.read()
    else:
        print(f"'{name}' does not exist")

# Delete an existing note
def delete_note():
    name = input("Note name: ")
    if os.path.exists(f"notes/{name}.md"):
        os.remove(f"notes/{name}.md")
        print(f"Successfully deleted '{name}'")
    else:
        print(f"'{name}' does not exist")

# List all notes in notes folder
def note_names():
    names = []
    files = os.listdir("notes")

    for file in files:
        if file[-3:] == ".md":
            names.append(file[:-3])
    
    return names

# Print UI (CLI only)
def ui():
    print("Choose action:")
    print("1. Create a new note")
    print("2. View a note")
    print("3. Delete a note")
    print("4. Show notes")
    print("0. End program")

if __name__ == "__main__":
    # CLI application main loop
    while True:
        ui()
        choice = input("Choice: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            name = input("Note name: ")
            content = view_note(name)
            print(f"'{name}' content:")
            print(content)
        elif choice == "3":
            delete_note()
        elif choice == "4":
            names = note_names()
            print("Notes:")
            for name in names:
                print(f"- {name}")
        elif choice == "0":
            break
        else:
            print("Invalid Input!")
        print()