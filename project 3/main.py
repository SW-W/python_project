from tkinter import *
import PyPDF2
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from functions import browse_file, copy_text, display_text, restart_gui, save_in_text_file


root = Tk()
root.title('PDF Text Extractor')
root.iconbitmap('pdf_aplicacion_1828.ico')

content = ''

def extract_text():
    global content
    global counter
    if content:
        content = ''
    if file_chosen.get() =='':
        messagebox.showerror(title='Error!',message='Please choose a pdf file first.')
    else:
        file = open(file_chosen.get(),'rb')
        if extract_page.get().isnumeric():
            page_to_extract = int(extract_page.get()) - 1
            try:
                read_pdf = PyPDF2.PdfFileReader(file)
                page = read_pdf.getPage(page_to_extract)
                page_content = page.extractText()
                content += page_content
                file.close()

                display_text(root,content)

                copy_but = Button(root, width=10, text='Copy', command=lambda:copy_text(root,content))
                copy_but.grid(row=3, column=2)

                restart_but= Button(root, width=10, text='Restart', command=lambda:restart_gui(file_chosen,extract_page,save_file,display_text, content, root))
                restart_but.grid(row=3, column=4)


            except IndexError:
                messagebox.showerror(title='Error!', message='Page number out of range.')

        else:
            messagebox.showerror(title='Error!',message='Please enter a page number.')


upper_left_frame = Frame(root, width=320, height=70)
upper_left_frame.grid(rowspan=1, columnspan=2, row=0, column=0)


lower_left_frame= Frame(root, width=320, height=200, bg='#7fdcec')
lower_left_frame.grid(row=1, column=0, rowspan=3, columnspan=2)


upper_right_frame = Frame(root, width=400, height=70)
upper_right_frame.grid(row=0, column=2, columnspan=3, rowspan=1)


lower_right_frame= Frame(root, width=400, height=200, bg='#7fdcec')
lower_right_frame.grid(row=1, column=2, columnspan=3, rowspan=3)


gui_name = Label(root, text='PDF TEXT EXTRACTOR', font=('Harrington',12,'bold'))
gui_name.grid(row=0, rowspan=1, column=0, sticky=W)


file_chosen =  Entry(root, width=25, font=('Arial',10))
file_chosen.grid(row= 1, column=0, sticky=W, padx=5, pady=5)


extract_page = Entry(root, width=25, font=('Arial',10))
extract_page.insert(0,'Page to extract')
extract_page.focus()
extract_page.grid(row=2, column=0, sticky=W, padx=5, pady=5)


save_file = Entry(root, width=25, font=('Arial',10))
save_file.grid(row=3, column=0, sticky=W, padx=5, pady=5)


browse_but = Button(root, width= 10, text='Browse', command=lambda:browse_file(file_chosen))
browse_but.grid(row= 1, column=1, sticky=W)


extract_but = Button(root, width= 10, text='Extract', command=lambda:extract_text())
extract_but.grid(row= 2, column=1, sticky=W)


save_but = Button(root, width= 10, text='Save',command=lambda:save_in_text_file(content,save_file))
save_but.grid(row= 3, column=1, sticky=W)

root.resizable(False,False)

root.mainloop()
