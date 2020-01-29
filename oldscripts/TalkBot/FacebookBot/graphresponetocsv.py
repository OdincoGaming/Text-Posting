import facebook
import json
import csv
import re

#{
# #############################
#}
# def's

#{
# #############################################################################################
# #############################################################################################
# }
# main

#file setup
graphresponse = open('graphresponse.txt','r')
contents = graphresponse.read()

outfile = open('csvtest.csv','w+')
writer = csv.writer(outfile, delimiter=':')

#clean data
jsdump = (json.dumps(contents, indent=4, separators=("':")))
jsdump = jsdump.split("\n")
#jsdump = str(jsdump)
#jsdump = jsdump.replace('\\','').replace('n','')
#jsdump = jsdump.split(",")
i = 0
for item in jsdump:
    print(item + str(i))
    i += 1

#save outfile
writer.writerows(jsdump)