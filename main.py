# Simple notetaking tool

# Print UI
def ui():
    print("Choose action:")
    print("1. Overwrite")
    print("2. Append")
    print("3. Quit")


try:
    with open("note.md", "r") as note:
        print("Current note:")
        print(note.read())
        ui()
        choice = input("Choice: ")
except FileNotFoundError:
    print("No existing notes")
    choice = "1"

if choice == "1":
    with open("note.md", "w") as note:
        while True:
            line = input()
            if line == "":
                break
            note.write(line + "\n")
elif choice == "2":
    with open("note.md", "a") as note:
        while True:
            line = input()
            if line == "":
                break
            note.write(line + "\n")
elif choice == "3":
    pass