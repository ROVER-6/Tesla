import os
os.system("title Tesla")

def cmd():
    print("-> 'help' to know how to use the shell")
    line = input("tesla -> ")
    if line == "help":
        print("type a normal cmd command and it will work here.\nyou can use 'clear' to clear the shell.\n")
        cmd()
    elif line == "clear":
        os.system("cls")
        cmd()
    else:
        os.system(line)
        cmd()

cmd()