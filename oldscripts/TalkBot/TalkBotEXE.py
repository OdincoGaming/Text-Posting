import google
import requests
from bs4 import BeautifulSoup
import TalkBotBrocas

contentList = []
textList = []
WordBank = open("WordBank.txt","w+")

def googleSearch(topic):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found")  
    query = topic 
    for j in search(query, tld="co.in", num=10, stop=3, pause=2): 
        print(j) 
        r=requests.get(j)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        CacheSearch(soup.get_text)
    
def CacheSearch(content):
    contentList.append(content)
    print((contentList))
    

#textList=contentList[count].find_all("p")
#WordBank.write(str(contentList[count].html.encode("utf8")))




topicIn = input("Pick A Topic ")
googleSearch(topicIn)
input("enter to exit")
