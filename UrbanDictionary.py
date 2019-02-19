import webbrowser
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

x = input("Welcome to the UrbanDictionary Search, what would you like to search for?\n")
webPageUrl = "https://www.urbandictionary.com/define.php?term=" + x
try:
    webPageInfo = urlopen(webPageUrl)
except HTTPError:
    print("This doesnt exist")
    quit()
    
meaning = ""

soup = BeautifulSoup(webPageInfo, 'html.parser')
moreSoup = soup.find('div', class_='meaning')

for c in moreSoup.contents:
    if c.string is not None:
        meaning += c.string
    
print(meaning)