import google
import requests
from bs4 import BeautifulSoup
import re
import string
import modules



def getTop10():
    yahoo = requests.get('https://www.yahoo.com/')
    rawsoup = yahoo.content
    soup = BeautifulSoup(rawsoup,'html.parser')
    top10 = []
    exclude = set(string.punctuation)
    top10soup = soup.find_all("li", {"class": "trending-list"})

    for i in top10soup:
        children = i.findChildren('a', recursive=True)
    for child in children:
        text = ''.join([c for c in child.text if not c.isdigit()])
        text = ''.join([c for c in text if c not in exclude])
        text = str.strip(text)
        top10.append(text + '\n')
        print(text)
    toptxtfile.writelines(top10)
    return top10

def googleSearch(topic, iterations):
    from googlesearch import search 
    print(topic + '\n')
    text = []
    for j in search(topic, tld="co.in", num=10, stop=iterations, pause=2): 
        print(j + '\n')
        r=requests.get(j)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        cleanSoup = soup

        for script in cleanSoup("script"):
            script.extract()
        for style in cleanSoup("style"):
            style.extract()
        for tag in cleanSoup(True):
            tag.unwrap()

        cleanSoup = modules.removetags(soup.prettify())
        #cleanSoup = cleanSoup.replace("\n","")

        finalText = str(cleanSoup.encode("utf8"))
        finalText = ''.join(i for i in finalText if  i.isalpha() or i == " " or i == "\n")

        text.append(finalText + '\n')

    texttxtfile.writelines(text)

toptxtfile = open('top10.txt','w+')
texttxtfile = open('top10text.txt','w+')
top10 = getTop10()
toptxtfile.close()
texttxtfile.close()

for i in top10:
    googleSearch(i, 3)