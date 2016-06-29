import re
import os

def openfile():
    file = open('castle.txt', 'r', encoding = 'utf-8')
    text = file.read()
    return text
    file.close()

def function1(text):
    regex = r"(\s[А-Я]\. ?[А-ЯЁ][а-яё]+)[.,):;\"—?!\s]"   
    print("\n".join(re.findall(regex, text)))
    
def function2(text):
    regex2 = r"([^.?!\n]*?( (?:[А-Я]\. ?)+[А-ЯЁ][а-яё]+)[.,)\]:;\"—?!\s][^.?!]*)"
    regex3 = r"([^.?!\n]*?([А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+)[.,)\]:;\"—?!\s][^.?!]*)"
    names = re.findall(regex2, text) + re.findall(regex3, text)
    print("\n".join([n[1] for n in names]))
    for n in names:
        surn = n[1].split()[-1]
        if not os.path.exists(surn):
            os.makedirs(surn)
        f = open(surn + '/' + n[1]+".txt", 'w', encoding = 'utf-8')
        f.write(n[0].strip())
        f.close()

if __name__ == "__main__":
    text = openfile()
    function1(text)
    function2(text)
