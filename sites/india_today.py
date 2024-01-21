import requests
from bs4 import BeautifulSoup

def today():
	url1 = 'https://www.indiatoday.in/technology/news'
	page = requests.get(url1)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='B1S3_content__wrap__9mSB6')
	List = []
	count=0
	s = ""
	
	for i in cl:
		Y=i.find("h2")
		count=count+1
		List.append(Y.get_text())	
	
	url= 'https://www.indiatoday.in/technology/news?page=1'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='catagory-listing')
	
	for i in cl:
		Y=i.find("h2")
		count=count+1
		if(count==18):
			break
		List.append(Y.get_text())
	for i in List:
		s = s + "\n🌐" + i
		
	return s