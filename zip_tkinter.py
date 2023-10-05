from tkinter import *
from tkinter import filedialog
from tkinter import font as tkfont
import tkinter as tk
import zipfile
import os

def zip_files():
    fp = filedialog.askopenfilenames(title="Select Files to Zip")
    if fp:
        zfn = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP Files", "*.zip")], title="Save Zip File As")
        if zfn:
            with zipfile.ZipFile(zfn, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in fp:
                    zipf.write(file, os.path.basename(file))
            status_label.config(text=f"Status: File zipped to {zfn}")

def unzip_files():
    zf = filedialog.askopenfilename(title="Select Zip File to Unzip", filetypes=[("ZIP Files", "*.zip")])
    if zf:
        unzf = filedialog.askdirectory(title="Select Folder to Unzip Files")
        if unzf:
            with zipfile.ZipFile(zf, 'r') as zipf:
                zipf.extractall(unzf)
            status_label.config(text=f"Status: File unzipped to {unzf}")

window = Tk()

frame = Frame(window)
frame.pack(padx=20, pady=20) 

labelframe1 = LabelFrame(frame, text="ZIP File here")
labelframe1.grid(row=0, column=0, padx=20, pady=20) 
label1 = Label(labelframe1, text="Select File/Folder for Zip: ",width=50).grid(row=0, column=0)  
btn1 = Button(labelframe1, text="Make Zip", command=zip_files).grid(row=1, column=0)

for widget in labelframe1.winfo_children():

    widget.grid_configure(padx=20,pady=15)


labelframe2 = LabelFrame(frame, text="UNZIP File here")
labelframe2.grid(row=1, column=0, padx=20, pady=20)  
label2 = Label(labelframe2, text="Select Workspace for UnZip: ",width=50).grid(row=0, column=0)  
btn2 = Button(labelframe2, text="Make UnZip", command=unzip_files).grid(row=1, column=0)

for widget in labelframe2.winfo_children():

    widget.grid_configure(padx=20,pady=15)

labelframe3 = LabelFrame(frame,text="Status")
labelframe3.grid(row=2,column=0, padx=20, pady=20)
status_label = Label(labelframe3, text="Status: Nothing Done Recently...",width=50)
status_label.grid(row=0, column=0)  

for widget in labelframe3.winfo_children():

    widget.grid_configure(padx=20,pady=15)

window.mainloop()
