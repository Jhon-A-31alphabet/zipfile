import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import zipfile


def make_zipfile():
    a = filedialog.asksaveasfile(defaultextension=".zip",filetypes=[("textfile",".zip")])
    zipfile.ZipFile(a,mode="w")
    

def compress_file():
    file_path = filedialog.askopenfilename()
    
    with zipfile.ZipFile(file_path + ".zip", "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path)


def py_tube_windw():
    #this function is for the second window to download videos....

    
    py_tube_window = tk.Toplevel()
   

    py_tube_window.resizable(False,False)
    py_tube_window.geometry("300x250")




    py_tube_window.configure(bg ="white")


    enter_link = tk.Entry(py_tube_window,borderwidth=10,relief="sunken",width=30)
    enter_link.place(x=50,y=110)
    button_to_download = tk.Button(py_tube_window,text="Download",command=lambda:download_video())
    button_to_download.place(x=50,y=150)


    main_massage = tk.Label(py_tube_window,text="YOUTUBE",padx=60,pady=20,bg="red",fg="white",font="arial 12",)
    main_massage.place(x= 40,y= 80)
    main_massage.pack()
    
    def download_video():
        get_l = enter_link.get()
        video = YouTube(get_l)
        stream = video.streams.get_lowest_resolution()
        stream.download()

    


