import json, os

os.system('cls') if 'nt' in os.name else os.system('clear')

subalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
others = [',','.',' ','!', "'",'"', ';',':']

dict = json.load(open('dict.json'))

string = list(input('string of letters: '))

for i in range(25):
    funny = 0
    step = (i + 1)
    oops = []
    for letter in string:
        if letter in others:
            oops.append(letter)
        else:
            if letter in subalpha:
                try:
                    oops.append(subalpha[subalpha.index(letter) + step])
                except:
                    pos = 26-subalpha.index(letter)
                    oops.append(subalpha[step-pos])
            else:
                try:
                    oops.append(upperalpha[subalpha.index(letter) + step])
                except:
                    pos = 26-upperalpha.index(letter)
                    oops.append(upperalpha[step-pos])
    
    words = "".join(x for x in oops)
    for char in others:
        words = words.replace(char, '#')
    words = words.split("#")
    for word in words:
        if word in dict:
            funny = 1
    if funny == 1:
        print("".join(x for x in oops))