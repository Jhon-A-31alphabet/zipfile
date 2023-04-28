import tkinter as tk
from tkinter import filedialog
import zipfile

def make_zipfile():
    a = filedialog.asksaveasfile(defaultextension=".zip",filetypes=[("textfile",".zip")])
    zipfile.ZipFile(a,mode="w")
    
    


    

