"""from bs4 import BeautifulSoup
import requests
def indian():
    url = "https://indianexpress.com/section/technology"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_='article-list')
    list = []
    s = ""
    news = cl[0].text
    news = news.split("\n\n\n\n\n\n\n\n")
    news[0] = news[0][7:]
    for i in news:
        s = s + i;
        #list.append(i)
    return s
    #return list
s = indian()
print(s)
"""
import requests
from bs4 import BeautifulSoup

def express():
    url = "https://indianexpress.com/section/technology"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_ = 'article-list')
    txt = cl[0].text
    cl = txt.split("\n\n\n\n\n\n\n\n")
    list = []
    s = ""
    for i in cl:
        list.append("\n")
        list.append(i)
    list[1] = list[1].replace("\n\n\n\n\n\n\n","")
    k = 0
    for i in list:
        if not k % 2 == 0:
            s = s + "\n🌐" + i
        k = k + 1
    return s