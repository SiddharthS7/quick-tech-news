from tkinter import Tk, END, INSERT, PhotoImage, Text, WORD, Button
from sites import (cnet, indian_express, ndtv, zee, india_today, live_mint)

root = Tk()
root.title("QuickTech News")
root.geometry("1920x1080")
root.state('zoomed')

def clear():
    text_box.configure(state = 'normal')
    text_box.delete(1.0, END)
    text_box.configure(state = 'disabled')

def a():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from NDTV Gadgets 💥☆☆☆☆☆")
    s = ndtv.ndtv()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

def b():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from Indian Express 💥☆☆☆☆☆")
    s = indian_express.express()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

def c():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from CNET 💥☆☆☆☆☆")
    s = cnet.cnet()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

def d():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from Zee 💥☆☆☆☆☆")
    s = zee.zee()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

def e():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from India Today 💥☆☆☆☆☆")
    s = india_today.today()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

def f():
    text_box.configure(state = 'normal')
    text_box.insert(INSERT, "\n\t\t\t\t☆☆☆☆☆💥 Fetching Tech News from Live Mint 💥☆☆☆☆☆")
    s = live_mint.mint()
    text_box.insert(INSERT, s)
    text_box.insert(INSERT, "\n")
    text_box.configure(state = 'disabled')

p1 = PhotoImage(file = r"icons/QuickTech Icon.png")
root.iconphoto(False, p1)

text_box = Text(root, height = 16, width = 114, font = ("Cascadia Code PL, Helvetica", 18), wrap = WORD, padx = 10, pady = 10, bd = 5, selectbackground = "blue")
text_box.place(x = 15, y = 330)
text_box.configure(state = 'disabled')

photo_ndtv = PhotoImage(file = r"icons/NDTV.png") 
photo_indian = PhotoImage(file = r"icons/INDIAN.png")
photo_cnet = PhotoImage(file =r"icons/CNET.png")
photo_zee = PhotoImage(file = r"icons/ZEE.png")
photo_today = PhotoImage(file = r"icons/TODAY.png")
photo_mint = PhotoImage(file = r"icons/MINT.png")
photo_clear = PhotoImage(file = r"icons/CLEAR.png")

button_ndtv = Button(root, image = photo_ndtv, bd = 2, command = a)
button_indian = Button(root, image = photo_indian, bd =2, command = b)
button_cnet = Button(root, image = photo_cnet, bd = 2, command = c)
button_zee = Button(root, image = photo_zee, bd = 2, command = d)
button_today = Button(root, image = photo_today, bd = 2, command = e)
button_mint = Button(root, image = photo_mint, bd = 2, command = f)
button_clear = Button(root, image = photo_clear, command = clear, bd = 5)

button_ndtv.place(x = 10, y = 10)
button_indian.place(x = 545, y = 15)
button_cnet.place(x = 1000, y = 10)
button_zee.place(x = 50, y = 150)
button_today.place(x = 480, y = 150)
button_mint.place(x = 1235, y = 15)
button_clear.place(x = 1015, y = 180)

root.mainloop()