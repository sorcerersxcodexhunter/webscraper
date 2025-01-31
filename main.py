
import requests

def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

                                                                                                       
url ="https://146.19.24.89/s?k=iphone&crid=3JEGODC1AVV8&sprefix=iphone%2Caps%2C660&ref=nb_sb_noss_1&__cpo=aHR0cHM6Ly93d3cuYW1hem9uLmlu"
fetchAndSaveToFile(url,"data/times.html")