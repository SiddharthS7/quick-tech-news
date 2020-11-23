import tkinter
from sites import (cnet,ndtv,indian_express)

window = tkinter.Tk()
window.title("PyTechNEWS")
window.geometry("1280x1920")

def a():
    s = ndtv.ndtv();
    self.mylabel = tkinter.Label(window, text = s).pack()
def b():
    list = indian_express.indian();
    for i in list:
        tkinter.Label(window, text = i).pack()
def c():
    list = cnet.cnet();
    for i in list:
        tkinter.Label(window, text = i).pack()
def clear(self):
    self.mylabel.pack_forget();

button_widget1 = tkinter.Button(window,text="NDTV",bg = "red", fg = "white", padx = 5, pady = 5, command = a).pack()
button_widget2 = tkinter.Button(window,text="Indian Express",bg = "green", fg = "white", padx = 5, pady = 5, command = b).pack()
button_widget3 = tkinter.Button(window,text="CNET",bg = "blue", fg = "white", padx = 5, pady = 5, command = b).pack()
clear = tkinter.Button(window, text="CLEAR", bg = "white", fg = "black", command = clear).pack()
tkinter.mainloop()