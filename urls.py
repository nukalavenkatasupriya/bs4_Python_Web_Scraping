from bs4 import BeautifulSoup
import requests
import csv
#url,req,soup
url="https://www.google.com/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

file=csv.writer(open("google.csv","w"))
file.writerow([soup.find_all('a')])    