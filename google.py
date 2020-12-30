from bs4 import BeautifulSoup
import requests

#url,req,soup
url="https://www.google.com/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)