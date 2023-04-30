import tkinter as tk
from tkinter import filedialog
import zipfile

def make_zipfile():
    a = filedialog.asksaveasfile(defaultextension=".zip",filetypes=[("textfile",".zip")])
    zipfile.ZipFile(a,mode="w")
    

def compress_file():
    file_path = filedialog.askopenfilename()
    
    with zipfile.ZipFile(file_path + ".zip", "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path)

    



    

