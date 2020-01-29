import google
import requests
from bs4 import BeautifulSoup
import re

TAG_RE = re.compile(r'<[^>]+>')
WordBank = open("WordBank.txt","w+")

def googleSearch(topic):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found")  
    query = topic 
    for j in search(query, tld="co.in", num=10, stop=25, pause=2): 
        print(j) 
#make html object
        r=requests.get(j)
        c=r.content
#make soup object
        soup=BeautifulSoup(c,"html.parser")
        cleanSoup = soup
#clean the soup
        for script in cleanSoup("script"):
            script.extract()
        for style in cleanSoup("style"):
            style.extract()
        for tag in cleanSoup(True):
            tag.unwrap()
#almost there
        cleanSoup = remove_tags(soup.prettify())
        cleanSoup = cleanSoup.replace("\n","")
        finalText = str(cleanSoup.encode("utf8"))     
#save the soup for later
        WordBank.write(finalText + "<|endoftext|>")

def remove_tags(text):
    return TAG_RE.sub('', text)

topicIn = input("Pick A Topic. ")
googleSearch(topicIn)
input("enter to exit")
