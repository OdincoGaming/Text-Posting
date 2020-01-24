import modules
import json
import csv
import random
import facebook
def getresponse():
    response = modules.gettextfromfile("txt","generatedtext.txt")
    return(response)
def getprompt():
    prompt = modules.gettextfromfile("txt","prompt.txt")
    return(prompt)
def changeprompt(prompt):
    modules.puttextinfile("txt","prompt.txt", prompt)

acctok = 'EAAKsaVifZCCYBALfzcVrZCDzVKbhJW1ZCTyPsd5g66bQ8M8iAxe9yN0qbtWutdu8XmfAoUpOoU31cELUQYLsAof481i4WmJNcPQBK6y8YiMQUoUWaBJ3ywZA9FjKGyJeXhFWcrph2uziSUQPNaADtzT2LFwqN3TfGIZBnABgf64XeU4tLOD1U'
idn = 110033357094675

def poststats():
    graph = facebook.GraphAPI(acctok)
    stats = graph.request('/me?fields=posts.limit(3){message,comments,reactions}')
    x = graph.request('/me?fields=posts.limit(3){message}')
    y = graph.request('/me?fields=posts.limit(3){comments,reactions}')
    return(x, y)
    
#me?fields=posts{message,comments,reactions}

x,y = poststats()
print(y)
print('\n\n')
print(x)

##################
# parsing through text to add to model, if randomly selected string from source
# has too many numbers or special characters it is not used
