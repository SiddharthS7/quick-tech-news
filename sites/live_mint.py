import requests
from bs4 import BeautifulSoup

def mint():
    url = 'https://www.livemint.com/technology/tech-news'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_ = 'headlineSec')
    List = []
    s = ""
    count = 0

    for i in cl:
        if("How" in i.text):
            continue
        count = count + 1
        if(count == 15):
            break
        if(i.text[-4:] == "2020"):
            List.append(i.text[:-24])
        else:
            List.append(i.text[:-25])
    for i in List:
        s = s + "\n🌐" + i
        
    return s