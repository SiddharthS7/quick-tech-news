from sites import (cnet,ndtv,indian_express)
import tkinter as tk
print("Welcome to news Bot")
site = input("1.NDTV Gadgets\n2.Indian Express Tech news\n3.CNET Tech news\nEnter your choice\n")
if (site == '1'):
    print('Fetching news from NDTV')
    list = ndtv.ndtv()
elif (site == '2'):
    print("Fetcing news from Indian Express")
    list = indian_express.indian()
elif (site == '3'):
    print("Fetching news from CNET")
    list = cnet.cnet()
else:
    print("Wrong choice\n")
    exit()
print("☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆")
for news in list:
    print("->",news)
