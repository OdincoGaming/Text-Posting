import random
import subprocess
import facebook
import google
import requests
from bs4 import BeautifulSoup
import re
import string
import pathlib
import json

acctok = 'EAAKsaVifZCCYBALfzcVrZCDzVKbhJW1ZCTyPsd5g66bQ8M8iAxe9yN0qbtWutdu8XmfAoUpOoU31cELUQYLsAof481i4WmJNcPQBK6y8YiMQUoUWaBJ3ywZA9FjKGyJeXhFWcrph2uziSUQPNaADtzT2LFwqN3TfGIZBnABgf64XeU4tLOD1U'
idn = 110033357094675
# END OF IMPORT
##############################################################################
##############################################################################
# WEB SEARCH
def googleSearch(topic, iterations):
    from googlesearch import search 
    print(topic + '\n')
    text = []
    texttxtfile = open(getfile("txt",'top10text.txt'))
    for j in search(topic, tld="co.in", num=10, stop=int(iterations), pause=2): 
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
        cleanSoup = removetags(soup.prettify())
        finalText = str(cleanSoup.encode("utf8"))
        finalText = ''.join(i for i in finalText if  i.isalpha() or i == " " or i == "\n")
        text.append(finalText + '\n')

    texttxtfile.close()

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
        top10.append(text)
    puttextinfile("txt","top10.txt", str(top10))
    return top10
# END OF WEB SEARCH
##############################################################################
##############################################################################
# WEB INTERACTIONS
def makepost(text):
    graph = facebook.GraphAPI(acctok)
    graph.put_object(parent_object='me', connection_name='feed',
    message=text)

def replytocomment(comment):
    graph = facebook.GraphAPI(acctok)
    return(1)

def getposts(page_id):
    graph = facebook.GraphAPI(acctok)
    posts = graph.get_object(id=page_id,fields='posts.fields(id)')
    postList=list(posts.values())
    postList = (json.dumps(postList, indent=4, separators=("':")))
    postList = ''.join([c for c in postList if c.isdigit() or c == ' ' or c == "\n" or c == "_"])
    postList = list(postList.split('\n'))
    postList = list(filter(str.strip,postList))
    l = len(postList)
    i = 0
    while i < l:
        postList[i] = ''.join(postList[i].split())
        i += 1
    return postList

def getpoststats(post_id):
    graph = facebook.GraphAPI(acctok)
    comments = graph.get_connections(id=post_id, connection_name='comments', include_hidden=True, order="reverse_chronological", filter='stream')
    reactions = graph.request('/' + post_id + '/reactions?summary=total_count')
    return(comments,reactions)
# END OF WEB INTERACTIONS
##############################################################################
##############################################################################
# TEXT GENERATION
def textgenerationu(length):
    string = 'python main.py --text "" --unconditional --length  '
    endindex = len(string) -1
    string = stringinsert(string, str(length), endindex)
    s = ''.join(c for c in string if not c == "\n")
    c = subprocess.call(s, shell=True)

def textgenerationi(prompt, length):
    string = 'python main.py --text "" --include True  --length  '
    string = stringinsert(string,prompt,23)
    endindex = len(string) -1
    string = stringinsert(string, str(length), endindex)
    s = ''.join(c for c in string if not c == "\n")
    c = subprocess.call(s, shell=True)

def textgeneration(prompt, length):
    string = 'python main.py --text "" --length  '
    string = stringinsert(string,prompt,23)
    endindex = len(string) -1
    string = stringinsert(string, str(length), endindex)
    s = ''.join(c for c in string if not c == "\n")
    c = subprocess.call(s, shell=True)

def polishtext():
    #returns a list of phrases
    text = gettextfromfile("txt",'generatedtext.txt')
    text = text.replace("\n","").replace("<|endoftext|>", " ")
    polishedtext = []
    ato = 0
    afrom = 0
    l = len(text)
    for c in text:
        ato += 1
        if c == "." or c == "?" or c == "!":
            polishedtext.append(text[afrom:ato])
            afrom = ato
        else:
            if ato == l:
                polishedtext.append(text[afrom:])
    return(polishedtext)

# END OF TEXT GENERATION
##############################################################################
##############################################################################



# UTILITIES
def stringinsert(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

def removetags(text):
    # used in googlesearch
    t = re.compile(r'<[^>]+>')
    return t.sub('', text)

def getfile(folder, filename):
    p = pathlib.Path(r'C:\Users\ThisPC\Downloads\Python\SocialMediaManager') / folder / filename
    return(p)

def gettextfromfile(folder, filename):
    p = pathlib.Path(r'C:\Users\ThisPC\Downloads\Python\SocialMediaManager') / folder / filename
    s = p.read_text()
    return(s)

def puttextinfile(folder, filename, string):
    p = pathlib.Path(r'C:\Users\ThisPC\Downloads\Python\SocialMediaManager') / folder / filename
    p.write_text(string)


############################################################################## 
modules = ["Web Search", "Web Interactions", "Text Generation", "Utilities"]
Web_Search = ["Google Search", "Top 10"]
Web_Interactions = ["Make Post", "Get Post ID's", "Get Post Stats"]
Text_Generation = ["Generate Text", "Polish Text"]
Utilities = ["Get File", "Get Text From File", "Put Text In File"]

##############################################################################
#Testing

def poststats(post_id):
    graph = facebook.GraphAPI(acctok)
    comments = graph.get_object(id=post_id, connection_name='comments')
    reactions = graph.request('/' + post_id + '/reactions?summary=total_count')
    return(comments,reactions)

##############################################################################