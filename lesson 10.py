# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code ==200:
#     soup =BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("a",{"href/currencies/bitcoin/#markets"})

from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
soup_list_name = soup.find_all('div',{"class":"th-title truncate"})
for i in soup_list_name:
    print(i.text)