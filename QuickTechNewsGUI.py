from tkinter import Tk, END, INSERT, PhotoImage, Text, WORD, Button, RIGHT, Scrollbar, Frame, messagebox
from sites import (cnet, indian_express, ndtv, zee, india_today, live_mint)

root = Tk()
root.title("QuickTech News")
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

def exit():
    root.destroy()

def info():
    messagebox.showinfo("Information", "->Click on any of the NEWS sources from the above displayed icons to get their latest Technology NEWS.\n->Click 'X' icon to clear the news.\n->Click exit if done.\U0001F606")

def about():
    messagebox.showinfo("About", "\tQuickTechNews\u00A9\n\nCreated by Siddharth Kumar Shakya\n\n\t          2020")

root.columnconfigure(0, pad = 3, weight = 1)
root.columnconfigure(1, pad = 3, weight = 1)
root.columnconfigure(2, pad = 3, weight = 1)
root.columnconfigure(3, pad = 3, weight = 1)
root.columnconfigure(4, pad = 3, weight = 1)
root.columnconfigure(5, pad = 3, weight = 1)
root.columnconfigure(6, pad = 3, weight = 1)
root.rowconfigure(0, pad = 3,weight = 0)
root.rowconfigure(1, pad = 3,weight = 1)
root.rowconfigure(2, pad = 3,weight = 1)
root.rowconfigure(3, pad = 3,weight = 1)

p1 = PhotoImage(file = r"icons/QuickTech Icon.png")
root.iconphoto(False, p1)

text_box = Text(root, font = ("Cascadia Code PL, Helvetica", 18), wrap = WORD, padx = 10, pady = 10, bd = 5, selectbackground = "blue")
text_box.configure(state = 'disabled')
text_box.grid(row = 3,column = 1 ,columnspan = 7, sticky = "nswe")

scrollbar = Scrollbar(root, command = text_box.yview)
text_box['yscroll'] = scrollbar.set
scrollbar.grid(row = 0,column = 8,rowspan = 4,sticky = "ns")

toolbar = Frame(root, borderwidth = 2,relief = 'raised')
toolbar.grid(row = 0, column = 0, rowspan = 4, columnspan = 1, sticky = "ns")
toolbar.columnconfigure(0, pad = 3, weight = 1)

help_btn = Button(toolbar, bd = 2, text = "Help",pady = 5, command = info)
about_btn = Button(toolbar, bd = 2, text = "About", pady = 5, command = about)
exit_btn = Button(toolbar, bd = 2, text = "Exit", pady = 5, command = exit)
help_btn.grid(row = 0, column = 0, sticky = "ew")
about_btn.grid(row = 1, column = 0, sticky = "ew")
exit_btn.grid(row = 2, column = 0, sticky = "ew")

photo_ndtv = PhotoImage(file = r"icons/NDTV.png") 
photo_indian = PhotoImage(file = r"icons/INDIAN.png")
photo_cnet = PhotoImage(file = r"icons/CNET.png")
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

button_ndtv.grid(row = 0, column = 1)
button_indian.grid(row = 0, column = 2)
button_cnet.grid(row = 0, column = 3)
button_zee.grid(row = 0, column = 4)
button_today.grid(row = 0, column = 5)
button_mint.grid(row = 0, column = 6)
button_clear.grid(row = 0, column = 7)

root.mainloop()