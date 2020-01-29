import facebook
import json
import csv
import re

#{
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# }

def GetMyId():
    myID = graph.request('/me?fields=id')
    ID = myID['id']
    print(ID)
    return ID

def GetPostIds(objectId):
    posts = graph.get_object(id=objectId,fields='posts.fields(id)')
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

def GetPostIdsToCSV(objectId):
    #infile
    f = open('PostIds.csv', 'w+')
    f2 = open('postidTest.txt', 'w+')
    #outfile
    of = csv.writer(f)

    posts = graph.get_object(id=objectId,fields='posts.fields(id)')
    postList=list(posts.values())
    postList = (json.dumps(postList, indent=4, separators=("':")))
    f2.write(postList)
    for post in postList:
        of.writerow(post)

    print(postList)
    f.close()
    f2.close()
    return postList

def GetPostReacts(objectId):
    reactList = graph.request('/' + objectId + '/reactions?summary=total_count')

    reactList = (json.dumps(reactList, indent=4, separators=('"_')))
    reactList = ''.join([c for c in reactList if c.isdigit() or c == ' ' or c == "\n" or c == "_"])
    reactList = list(reactList.split('\n'))
    reactList = list(filter(str.strip,reactList))

    reacts = reactList[-1]
    reacts = ''.join([c for c in reacts if c.isdigit()])

    print(reacts)
    return reacts

def GetPostComments(objectId):
    comments = graph.get_connections(id=objectId, connection_name='comments', include_hidden=True, order="reverse_chronological", filter='stream')
    print(comments)
    return(comments)

def GetPageIds(objectId):
    pages = graph.get_object(id=objectId,fields='likes.fields(id)')
    pageList=list(pages.values())
    pageList = (json.dumps(pageList, indent=4, separators=("':")))
    pageList = ''.join([c for c in pageList if c.isdigit() or c == ' ' or c == "\n" or c == "_"])
    pageList = list(pageList.split('\n'))
    pageList = list(filter(str.strip,pageList))

    l = len(pageList)
    i = 0
    while i < l:
        pageList[i] = ''.join(pageList[i].split())
        i += 1

    return pageList

#{
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# }

token = "EAAKsaVifZCCYBAOCwOg2w5IDifnnm8VCa43s2DyNH21tpdKSyawZACdBzpLlofIr43XCEaMwDXx5YgJpQOmzijwKy32btBH6j1m9Cdo1MqNs6c13nuTfj2UYzkg4aI3qBfqegNgb4OREfQZCZBc7oDDHFZAGttdNQzrPbHNPz5ahFZCsOU2IgU"
graph = facebook.GraphAPI(token)
ID = "2894021623958853"
post = "2894021623958853_2944241765603505"
#likes = GetPageIds(ID)
#posts = GetPostIds(ID)
comments = GetPostComments(post)
print(comments)



