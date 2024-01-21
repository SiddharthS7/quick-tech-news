import requests
from bs4 import BeautifulSoup

def mint():
    url = 'https://www.livemint.com/technology/tech-news'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_ = 'headline')
    List = []
    s = ""
    count = 0

    List = [i.findChildren('a')[0].text for i in cl]

    for i in List:
        s = s + "\n🌐" + i
        
    return s