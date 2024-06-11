import requests
from bs4 import BeautifulSoup

class WebScrapper:
    def __init__(self,url):
        self.url=url
    def get_page_content(self):
        response=requests.get(self.url)
        return BeautifulSoup(response.text,'html.parser')
    def extra_data(self):
        soup=self.get_page_content()
        data=[]
        for link in soup.find_all('a'):
            data.append(link.get('href'))
        return data

scraper=WebScrapper("http://192.168.0.170:5500/All.html")
print(scraper.extra_data())