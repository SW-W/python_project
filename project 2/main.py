from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Watermark Generator')
root.minsize(width=450, height=450)
root.config(padx=20, pady=20)

choose_photo = Entry(width=60)
choose_photo.grid(row=0, column=0)

def chosen_pic():
    pic = fd.askopenfilename(title='Choose a picture')
    choose_photo.insert(0,pic)
    if choose_photo.get() == "":
        messagebox.showerror('Error','Please choose a picture')
    else:  
        decided_pic = Image.open(choose_photo.get())
        resized_pic = decided_pic.resize((300,300))     
        im = ImageTk.PhotoImage(resized_pic)
        label1= Label(image=im)
        label1.image = im
        label1.grid(row=1, column=0, sticky='nsew',pady=10, columnspan=3)
        messagebox.showinfo('Picture Confirmation','Please make sure the correct picture has been selected.')


browse_but= Button(text='Browse', command=chosen_pic)
browse_but.grid(row=0, column=1, padx=10)

def add_mark():
    if choose_photo.get() == "":
        messagebox.showerror('Error','Please choose a picture')
    else:
        fpic = Image.open(choose_photo.get())
        watermark = Image.open('watermark.png')      
        watermark = watermark.resize(fpic.size)
        fpic.paste(watermark, (0,0), mask=watermark)
        return fpic

add_watermark_but = Button(text='Add watermark', command=add_mark)
add_watermark_but.grid(row=2, column=0, columnspan=4)

def save_pic():
    if add_mark():
        final_pic = add_mark()
        folder = fd.askdirectory(title='Select the folder to save the picture')
        final_pic = final_pic.save(folder + '/watermark_added_pic.png')
        messagebox.showinfo('Saved','Picture has been saved in desired folder.')
        choose_photo.delete(0,END)


save_but = Button(text='Save', command=save_pic)
save_but.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()
