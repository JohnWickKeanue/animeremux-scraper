import time
from bs4 import BeautifulSoup
import requests

url = "https://www.animeremux.xyz/2022/07/my-dress-up-darling-2022-anime-series.html?m=1"

def remux(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    for a in soup.find_all("a"):
             c = a.get("href") 
             if "urlshortx.com" in c:
                      x = c.split("url=")[-1]
                      t = client.get(x).text
                      soupt = BeautifulSoup(t, "html.parser")
                      title = soupt.title
                      gd_txt = f"{(title.text).replace('GDToT | ' , '')}\n{x}\n\n"
                      print(gd_txt) 

print(remux(url))
