import sys

if len(sys.argv) != 2 or sys.argv[1] != "banned.txt":
    sys.exit("Usage: python bleep.py banned.txt")

nnw = []
nono_words = open(sys.argv[1]).readlines()
for w in nono_words:
    w = w.rstrip('\n')
    w = w.lower()
    nnw.append(w)

#text = input("input your text: ")
text = "your mom is so gosh darn awesome"
l = text.split()
print(l)

clean_text = []
for w in l:
    if w in nnw:
        s = ''
        for i in range(len(w)):
            s = s+'*'
        w = s
    clean_text.append(w)
    print(w)
