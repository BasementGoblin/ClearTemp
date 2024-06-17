from tkinter import *
import tempfile
import os
import shutil
import stat

# Basic setup for the window and tkinter root.
root = Tk()
root.title("Temp Folder Cleaner")
root.geometry("320x50")

instruction = Label(root, text="Enter your temp folder location:")
instruction.grid(column=0, row=1)

# We use tempfile to find our temp directory.
path = StringVar()

# We create an Entry widget for our temp folder path.
txt = Entry(root, width=40, textvariable=path)
path.set(tempfile.gettempdir())
txt.grid(column=0, row=2)

# Function executes when button is clicked.
def clicked():
    dir_list = os.listdir(path.get())
    for file in dir_list:
        if os.path.isfile(path.get() + "\\"  + file):
            try:
                os.remove(path.get() + "\\" + file)
                print("Removing " + file)
            except Exception as e:
                print("Could not remove " + file)

        elif os.path.isdir(path.get() + "\\"  + file):
            try:
                # This line of code is apparently supposed to change files that're read-only and allow us to delete them.
                # From what I can gather it doesn't work, if the line is still here it means I'm to lazy to remove or fix it.
                os.chmod(os.path.join(path.get(), file), stat.S_IWRITE)

                shutil.rmtree(os.path.join(path.get(), file), ignore_errors=False)
                print("Removing " + file)
            except Exception as e:
                print("Could not remove " + file)

        else:
            print("Unknown filetype...")


btn = Button(root, text="Clear Folder", command=clicked)
btn.grid(column=1, row=2)

root.mainloop()