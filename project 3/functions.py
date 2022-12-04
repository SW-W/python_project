from tkinter import *
from tkinter import filedialog


def browse_file(entry):
    selected_file = filedialog.askopenfilename(filetypes=[("Pdf file", "*.pdf")])
    entry.insert(0,selected_file)


def copy_text(root,content):
    root.clipboard_clear()
    root.clipboard_append(content)


def restart_gui(entry1, entry2, entry3,display_text,content, root):
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    content=''
    display_text(root,content)


def display_text(root,content):
    textbox = Text(root, width=50, height=10)
    textbox.insert(1.0, content)
    # curly bracket exist when a list being passed
    textbox.grid(row=1, column=2, columnspan=3, rowspan=2, pady=15, padx=15)


def save_in_text_file(content, save_file):
    folder = filedialog.askdirectory()
    save_file.insert(0,folder)
    file=open(f'{folder}/Saved Text.txt','w')
    file.write(content)
    file.close()

