from bs4 import BeautifulSoup
import requests
def ndtv():
    url = "https://gadgets.ndtv.com/news"
    page = requests.get(url)
    s = ""
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_='news_listing')
    for i in cl:
        s = s + ("\n🌐"+i.text)
    return s 
