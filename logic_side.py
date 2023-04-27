import tkinter as tk
import zipfile

def make_zipfile(zipfle):
    zipfile.ZipFile(f"{zipfle}.zip","w")
    

