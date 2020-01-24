import random
import subprocess

dataset = open('\txt\top10text.txt','r')
promptFile = open('\txt\prompt.txt', 'w+')

def createPrompt():
    line = dataset.readline()

    cnt = 1
    done = None
    prompt = None
    while cnt < 30 or done == None:
        line = dataset.readline()
        lineLen = len(line)
        length = random.randint(36,int((lineLen*.4)+ 36))
        #safe reading habits
        padding = lineLen - length
        if padding <= 0:
            padding = 1    
        startingChar = random.randint(0,padding)
        #read line
        text = line[startingChar:startingChar+length]
        #randomization of chosen line
        coin = random.randint(0,99)
        if cnt < 20 and coin > 74:
            done = True
            prompt = text
        elif cnt < 34 and coin > 60:
            done = True
            prompt = text
        else:
            done = True
            prompt = text
        cnt += 1
    promptFile.write(prompt)
    return(prompt)

def GenerateTipOfTheDay():
    rs = random.randint(6,24) 
    rs = str(rs)
    ri = int(rs)
    i = 0
    while i < ri//2:
        c = subprocess.call('python main.py --text "The tip of the day is; " --include True --length ' + rs, shell=True)
        i += 1
        print("\n" + i + "th iteration \n")

def GenerateWhatYourMomSaid():
    ri = random.randint(6,36) 
    rs = str(ri)
    i = 0
    done = False
    while i < ri//2:
        coin = random.randint(0,4)
        if i >(ri//2)-2 and done == False or coin > 3 and done == False:
            c = subprocess.call('python main.py --text "Your mom said " --include True --length ' + rs, shell=True)
            done = True
        i += 1
        print("\n" + str(i) + "th iteration \n")

def GenerateTopSearchComment():
    done = False
    with open('\txt\top10.txt') as f:
        for cnt, line in enumerate(f):
            ri = random.randint(12, 42)
            rs = str(ri)
            coin = random.randint(0,9)
            string = 'python main.py --text "" --include False --length  '
            string = stringinsert(string, line, 23)
            string = stringinsert(string, rs, 43)
            print(string)
            if cnt > 8 and done == False or coin > 4 and done == False:
                c = subprocess.call(string, shell=True)
                done = True

def test():
    with open('\txt\top10.txt') as f:
        done = False
        d = 0
        for cnt, line in enumerate(f):
            length = random.randint(7,40)
            coin = random.randint(0,9)
            s = line
            if cnt > 8 and done == False or coin > 7 and done == False:
                string = 'python main.py --text "" --include False --length  '
                string = stringinsert(string,s,23)
                endindex = len(string) -1
                string = stringinsert(string, str(length), endindex)
                s = ''.join(c for c in string if not c == "\n")
                done = True
            if done == True and d == 0:
                print('\n' + s + '\n')
                c = subprocess.call(s, shell=True)
                d += 1
        f.close()

def stringinsert(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

test()

#GenerateTopSearchComment()
#GenerateWhatYourMomSaid()