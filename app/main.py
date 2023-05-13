import tkinter as tk
from logic_side import *


class ui:
    def __init__(self,master):
        master.resizable(False,False)

        
        self.background = master.configure(bg = "#cd3080")

        self.size_ = master.geometry("250x250")
        self.button_compress =tk.Button(master,text ="compress",borderwidth=5,relief="groove",bg="cyan",fg = "green",command=compress_file)
        
        self.button_compress.place(x=50,y=85)
        
        self.button_open= tk.Button(master,text="make",borderwidth=5,relief="groove",command=make_zipfile,bg="yellow",fg="black")
        self.button_open.place(x=120,y=85)

        self.url_linker = tk.Button(master,text="download video",borderwidth=5,relief="groove",bg="pink",fg="black",font="Arial")
        self.url_linker.place(x=50,y=10)
    

    
root = tk.Tk()
root.title("Z V DOW")
f = ui(root)
root.mainloop()
        


        
    
        



