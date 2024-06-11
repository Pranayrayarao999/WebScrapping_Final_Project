import requests
from bs4 import BeautifulSoup

#http://192.168.0.170:5500/RecordsTable.html
r=requests.get("http://192.168.0.170:5500/RecordsTable.html")
print(r.text)
r_html=r.text
soup=BeautifulSoup(r_html,'html.parser')

#find all the product names and prices
product_names=[product.text for product in soup.find_all('td',class_="product-name")]
product_price=[product.text for product in soup.find_all('td',class_="product-price")]
for name,price in zip(product_names,product_price):
    print(f'Product Name :{name}, Product Price:{price}')