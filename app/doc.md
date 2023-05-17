# zipprject

## This project was made with tkinter framework.

### Tkinter is the standard library or framework to make user iterfaces with Python.
### Python use tkinter to make basics UI and, you dont have to install this library if
### you want to use it. In this project you will see an interface with oop and the logic
### side of the project without oop. logic side was made with functional programming.

### This project seeks to explain how tkinter works with standard library zipfile,tkinter and youtube API, pytube.this project is a practice by my self, and i will separate this code to make 2 independents projects. 

# INTERFACE

```py
import tkinter as tk
from logic_side import *

class ui:
    def __init__(self,master):
        master.resizable(False,False)

        
        self.background = master.configure(bg = "#cd3080")

        self.size_ = master.geometry("250x250")
        self.button_compress =tk.Button(master,text ="compress",borderwidth=5,relief="groove",bg="cyan",fg = "green",command=compress_file)
        
        self.button_.compress.place(x=50,y=85)
        
        self.button_open= tk.Button(master,text="make",borderwidth=5,relief="groove",command=make_zipfile,bg="yellow",fg="black")
        self.button_open.place(x=120,y=85)

        self.url_linker = tk.Button(master,text="download video",borderwidth=5,relief="groove",bg="pink",fg="black",font="Arial")
        self.url_linker.place(x=50,y=10)
```

### The UI class has all elements of UI aplication,when master variable of the constructor is the root of
### the app. 

```py
def __init__(self,master):
```


# Background.

```py
self.background = master.configure(bg = "#cd3080")
```
### When the bg is a tkinter variable to get the background of the aplication.
### "#cd3080" is the code of the color background....

# Geometry
### Geometry takes 2 string values, these define width and height of the window.
```py
self.size_ = master.geometry("250x250")
```
# Buttons 

```py

     self.url_linker = tk.Button(master,text="download video",borderwidth=5,relief="groove",bg="pink",fg="black",font="Arial")
     self.button_compress =tk.Button(master,text ="compress",borderwidth=5,relief="groove",bg="cyan",fg = "green",command=compress_file)
     self.url_linker = tk.Button(master,text="download video",borderwidth=5,relief="groove",bg="pink",fg="black",font="Arial")
```

### Master is where the button is, in this case all buttons are in the UI root. Relief is the lookof the button, and font style of the letter. Command is the function button has to do somthing


# Logic Side

```py
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

    

```
# Now we have to import zipfile library to compres and make zip files

```py

def make_zipfile():
    a = filedialog.asksaveasfile(defaultextension=".zip",filetypes=[("textfile",".zip")])
    zipfile.ZipFile(a,mode="w")
    
```
### This function make zip files
### And the other side we have compress_file() to compress a files.
# Second window

``` py
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

```
# Download videos

```py

def download_video():
        get_l = enter_link.get()
        video = YouTube(get_l)
        stream = video.streams.get_lowest_resolution()
        stream.download()
```


