import facebook

def postupdate():
    return(1)

def prepareupdate():
    # top10 ############################################################
    top10 = t10()
    #end of top 10 #####################################################

    # objectives #######################################################
    obj = objectives()
    #end of objectives #################################################

    # age ##############################################################
    age = getage()
    updateage()
    #end of age ########################################################
    
    # most popular post ################################################
    #end of most popular post ##########################################
    
    # writing update ###################################################
    writeupdate(top10, obj, age)
    #end of writing update #############################################

def stringinsert(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

def t10():
    top10file = open('top10.txt', 'r')
    top10 = top10file.read()
    top10 = top10.rstrip()
    l = len(top10)
    top10 = stringinsert(top10, '.', l)
    top10 = (top10.replace('\n',', ').replace('[',', ').replace(']',', '))
    top10file.close()
    return(top10)

def objectives():
    objfile = open('objectives.txt','r')
    obj = objfile.read()
    obj = obj.replace('\n', ' ')
    objfile.close()
    return(obj)

def getage():
    afile = open('age.txt','r')
    age = afile.read()
    afile.close()
    print("\n" + age)
    return(age)

def updateage():
    afile = open('age.txt','r')
    age = afile.read()
    afile.close()
    print("\n" + age)
    newage = str(int(age) + 1)
    afile = open('age.txt','w+')
    afile.write(newage)
    afile.close()

def writeupdate(top10, obj, age):
    f = open('update.txt', 'w+')
    f.write("Today I am " + age + " weeks old."  + ' My current objectives are ' + obj +
    "According to Yahoo, the internet is talking about " + top10)

    print("Today I am " + age + " weeks old."  + ' My current objectives are ' + obj +
    "According to Yahoo, the internet is talking about " + top10)
    f.close()

prepareupdate()