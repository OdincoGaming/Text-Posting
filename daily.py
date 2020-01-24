import modules
import random


def changeprompt(prompt):
    modules.puttextinfile("txt","prompt.txt", prompt)
def getprompt():
    prompt = modules.gettextfromfile("txt","prompt.txt")
    return(prompt)
def getresponse():
    response = modules.gettextfromfile("txt","generatedtext.txt")
    return(response)

def top10post():
    top10 = modules.getTop10()
    toptext = "Today, according to Yahoo, the internet is searching for " + (', '.join(top10))
    modules.makepost(toptext)
    changeprompt(top10[random.randint(0,9)] + ", ")
    prompt = getprompt()
    modules.textgenerationi(prompt, random.randint(12,120))
    response = modules.polishtext()
    r = ""
    for s in response:
        r += " " + s
    modules.makepost(r)

def gimmickpost():
    dice = random.randint(0,3)
    if dice == 0:
        #when you
        modules.textgenerationi("When you ", random.randint(6,36))
        response = getresponse()
        modules.makepost(response)
    elif dice == 1:
        #your mom said
        modules.textgenerationi("Your mom said ", random.randint(6,36))
        response = getresponse()
        modules.makepost(response)
    elif dice == 2:
        #tip of the day
        modules.textgenerationi("The tip of the day is ", random.randint(6,36))
        response = getresponse()
        modules.makepost(response)
    elif dice == 3:
        #what if
        modules.textgenerationi("What if ", random.randint(6,36))
        response = getresponse()
        modules.makepost(response)

def randompost():
    postcount = random.randint(1,3)
    i = 0
    while i < postcount:
        modules.textgenerationu(random.randint(12,36))
        text = modules.polishtext()
        t = ""
        j = 0
        for c in text:
            if j == 0:
                t += t + c
            else:
                t += t + " " + c
        modules.makepost(t)
        i += 1
        print("\npost count: " + str(postcount) + "\n" + "i " + str(i))



top10post()
gimmickpost()
randompost()

