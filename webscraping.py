import requests ,lxml
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import datetime

now = datetime.datetime.now()
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:10809"
}

data = {'title':[],'price':[],'Date':now}
                                                               
url ="https://www.amazon.in/s?k=smartphone&crid=TJ958GX0ARF2&sprefix=smartpho%2Caps%2C309&ref=nb_sb_ss_ts-doa-p_2_8"
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def extract_text(soup,selector):
    try:
        return soup.select_one(selector).get_text().strip()
    except AttributeError as err:
        print(err)
        return None

r=requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,'lxml')
#print(soup.prettify())
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)
for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["price"].append(price.find("span").get_text())
        if (len(data["price"]) ==len(data["title"])):
            break

df = pd.DataFrame.from_dict(data)

df.to_csv("data.csv",index=False)

conn = sqlite3.connect('scraper.db')
c = conn.cursor()
df.columns = df.columns.str.strip()
#c.execute('''CREATE TABLE Prices(Product TEXT,price REAL)''')
df.to_sql('Prices',conn,if_exists="replace")

print("connect")
conn.close()