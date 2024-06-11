# http://192.168.0.170:5500/All.html
#Make sure the website is running, then copy the link

import requests
from bs4 import BeautifulSoup

url=requests.get("http://192.168.0.170:5500/All.html")
print(url.text)  #you can see the total data of the webpage
print(url.content)     #you can see entire content

#Get title tag and content
soup=BeautifulSoup(url.text,'html.parser')
print(soup.title)     #you can see the title tag and title name

#get only tag name
print(soup.title.name) #only title is visible   (title)

#get title tag and content in array format
print(soup.select('title'))       #[<title>Web Page</title>]

#select all p tags
print(soup.select('p'))     # displays all p tags and content inside it

#select all class attributes with name'.nav-item' and content in that
print(soup.select('.nav-item'))

#get single p tag and inside content using index position
print(soup.select('p')[0])

#get single p tag and inside content using index position
print(soup.select('p')[0].getText())

#select the p tags and content using slicing
print(soup.select('p')[0:4])

#select only content with class attribute name '.nav-link' using for loop
for i in soup.select('.nav-link'):
    print(i.text)

#select only single 'a' tag
print(soup.a)

#select all 'a' tags and content
all_a=soup.find_all(name_='a')
print(all_a)

#select only content from 'p' tag using for loop
all_p=soup.find_all(name='p')
for tag in all_p:
    print(tag.get_text())

#select id attribute with name loginEmail and password
form=soup.find(id="loginEmail")
print(form)
form =soup.find(id="loginPassword")
print(form)

#select single class attribute with name 'card title'
s=soup.find(class_='card-title')
print(s)
print(s.name)
print(s.get('class'))

#select all class attributes with name 'card-title' and tag name hs
s=soup.find_all('h5',class_='card-title')
print(s)

#select all id attributes with name 'navbarNav/'
s=soup.select_one(selector= '#navbarNav')
print(s)

#select the img tag using index position
print(soup.select('img')[2])

#select the image tag attribute like src and alt using index position
s=soup.select('img')[2]
print(s['alt'])
print(s['src'])

