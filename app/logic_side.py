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



"""""

def other_window():
    ventana_secundaria = tk.Toplevel(ventana_principal)
    ventana_secundaria.title("Ventana Secundaria")
    # Personaliza la ventana secundaria según tus necesidades
    # ...
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")
    boton = tk.Button(ventana_principal, text="Abrir ventana secundaria", command=crear_ventana_secundaria)
    boton.pack()
    ventana_principal.mainloop()

"""

    

