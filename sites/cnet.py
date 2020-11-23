from bs4 import BeautifulSoup
import requests
def cnet():
    url = "https://www.cnet.com/news/"
    page = requests.get(url)
    #list = []
    s = ""
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_='assetHed')
    for i in range(0,10):
        s = s + ("\n🌐"+cl[i].text)
        #list.append(cl[i].text)
    return s
    #return list
s = cnet()
print(s);