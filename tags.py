import requests
from bs4 import BeautifulSoup
with open("sample.html","r") as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.div.string)



