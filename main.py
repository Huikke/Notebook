# Simple notetaking tool
try:
    with open("note.md", "r") as note:
        print("Current note:")
        print(note.read())
        new_note = input("Edit note? (yes/no): ")
except FileNotFoundError:
    print("No existing notes")
    new_note = "yes"

if new_note == "yes" or new_note == "y":
    with open("note.md", "w") as note:
        note.write(input("Write note: "))