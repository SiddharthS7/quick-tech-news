from bs4 import BeautifulSoup
import requests

def cnet():
    url = "https://www.cnet.com/tech/"
    page = requests.get(url)
    s = ""
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_='c-dynamicDoorCard_title')

    for i in range(0,10):
        s = s + ("\n🌐"+cl[i].text)
    
    return s