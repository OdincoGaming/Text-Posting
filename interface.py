import modules

############################################################################

def restart():
    main()

def main():
    print("\n")
    c = 0
    for i in modules.modules:
        print("press [" + str(c) + "] for " + i)
        c += 1
    print("press [" + str(c) + "] to quit")
    #--------------------------------------------
    #--------------------------------------------
    selection = input('\nto continue, make a selection\n')
    if selection == "0":
        websearch()
    elif selection == "1":
        webinteractions()
    elif selection == "2":
        textgeneration()
    elif selection == "3":
        utilities()
    elif selection == "4":
        closeinterface()
    else:
        print("invalid selection")
        y = input("press y to exit\n")
        if y == 'y' or y == 'Y': 
            closeinterface()
        else:
            restart()
    #--------------------------------------------
        return(1)

def websearch():
    print("\n")
    c = 0
    for i in modules.Web_Search:
        print("press [" + str(c) + "] for " + i)
        c += 1
    print("press [" + str(c) + "] for menu")
    #--------------------------------------------
    #--------------------------------------------
    selection = input("\nto continue, make a selection\n")
    if selection == "0":
        topic = input("what to search for ")
        iterations = input("how many results ")
        modules.googleSearch(topic, iterations)
        websearch()
    elif selection == "1":
        top10 = modules.getTop10()
        websearch()
    else:
        print("invalid selection, returning to main")
        restart()
    #--------------------------------------------
    websearch()

def webinteractions():
    print("\n")
    c = 0
    for i in modules.Web_Interactions:
        print("press [" + str(c) + "] for " + i)
        c += 1
    print("press [" + str(c) + "] for menu")
    #--------------------------------------------
    #--------------------------------------------
    selection = input('\nto continue, make a selection\n')
    if selection == "0":
        modules.makepost()
        webinteractions()
    elif selection == "1":
        p = modules.getposts(modules.idn)
        for i in p:
            print(i)
        webinteractions()
    elif selection == "2":
        post_id = input("what post id ")
        c,r = modules.getpoststats(post_id)
        for i in c:
            for j in r:
                print(i + " " + j)
        webinteractions()
    elif selection == "3":
        restart()
    else:
        print("invalid selection")
        y = input("press y to exit\n")
        if y == 'y' or y == 'Y': 
            closeinterface()
        else:
            restart()
    #--------------------------------------------
    webinteractions()

def textgeneration():
    print("\n")
    c = 0
    for i in modules.Text_Generation:
        print("press [" + str(c) + "] for " + i)
        c += 1
    print("press [" + str(c) + "] for menu")
    #--------------------------------------------
    #--------------------------------------------
    selection = input("\nto continue, make a selection\n")
    if selection == "0":
        prompt = modules.gettextfromfile("txt", "prompt.txt")
        include = input("include prompt in response? y/n\n")
        length = input("length of response ")
        if include == "y" or "Y":
            modules.textgenerationi(prompt, length)
        else:
            modules.textgeneration(prompt, length)
        print(modules.gettextfromfile("txt","generatedtext.txt") + "\nyeeeet")
        textgeneration()
    elif selection == "1":
        t = modules.polishtext()
        print(t)
        textgeneration()
    elif selection == "2":
        restart()
    else:
        print("invalid selection, returning to main")
        restart()
    #--------------------------------------------
    textgeneration()

def utilities():
    print("\n")
    c = 0
    for i in modules.Utilities:
        print("press [" + str(c) + "] for " + i)
        c += 1
    print("press [" + str(c) + "] for menu")
    #--------------------------------------------
    #--------------------------------------------
    selection = input('\nto continue, make a selection\n')
    if selection == "0":
        folder = input("what folder ")
        file = input("what file ")
        f = modules.getfile(folder, file)
        print(f)
        utilities()
    elif selection == "1":
        folder = input("what folder ")
        file = input("what file ")
        f = modules.gettextfromfile(folder, file)
        print(f)
        utilities()
    elif selection == "2":
        folder = input("what folder ")
        file = input("what file ")
        text = input("what to write ")
        modules.puttextinfile(folder, file, text)
        print(modules.gettextfromfile(folder, file))
        utilities()
    elif selection == "3":
        restart()
    else:
        print("invalid selection")
        y = input("press y to exit\n")
        if y == 'y' or y == 'Y': 
            closeinterface()
        else:
            restart()
    #--------------------------------------------
    restart()

def closeinterface():
    exit()

############################################################################

#
##
###
####
#####

## "Welcome to my soul" said the robot
main()

#####
####
###
##
#

############################################################################
