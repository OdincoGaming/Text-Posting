import json
import facebook
import re
from collections import OrderedDict

def returnIds(listofIds):
    idsDict = OrderedDict(listofIds)
    ids = json.dumps(listofIds,indent=4)

    #ids = ''.join(i for i in ids if i.isdigit())
    #ids = re.sub("(.{64})", "\\1\n", ids, 0, re.DOTALL)
    #ids = re.sub("\D", "", ids)


    return ids

def main():
    token = {'EAAKsaVifZCCYBACB1mPP3935nmW5Yps9ZCG2Kl9IIl8sZCeSEf5dT79MmDqXfRCL24OhdjSfTBUwQZCZAcX6A0Y7dTu6WCpW3xrjWI4ZBKuDAZBGT4T58Y3sgNseZBmjLFZBiD9ZBbJoT9ECWdd5tFZBZBPyY4R4rjzFPxzxqDyKHLXwsyhNJ3D6hhDknNBylIaZBJgxuMxyzX5NjZCwZDZD'}
    graph = facebook.GraphAPI(token)
    pagesLiked = graph.get_object('me',fields='likes{id}')
    pageIds = returnIds(pagesLiked)

    #print(json.dumps(pagesLiked,indent=4))

if __name__ == "__main__":
    main()