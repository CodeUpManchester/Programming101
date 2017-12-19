#from win32com.client import constants
#import win32com.client
from sets import Set

sowpods = []
#speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    print text
    #speaker.Speak(text)

class ScrabbleHelper:

    def __init__(self):
        say("Loading Scrabble dictionary...")
        f = open("sowpods.txt", "r")
        line = "start"
        while line != "":
            line = f.readline()
            sowpods.append(line.strip().lower())
        f.close()
        say("OK, I'm ready.")

    def checkDictionary(self, word):
        if word in sowpods:
            say("Yes, " + word + " can be used in Scrabble.")
        else:
            say("No, " + word + " cannot be used in Scrabble.")
    
    def makeWords(self, text):
        tiles = text.split()
        if len(tiles) == 0:
            say("You didn't give me any letters to work with.")
            return
        
        say("Give me a moment to think...")

        speech = tiles[0]
        if len(tiles) == 1:
            if tiles[0] in sowpods:
                say(tiles[0] + " can be used on its own in Scrabble.")
            else:
                say(tiles[0] + " cannot be used on its own in Scrabble.")
            return
        else:
            for letter in tiles[1:-1]:
                speech = speech + ", " + letter
            speech += " and " + tiles[-1]
            speech = "Using the letters " + speech + " you can make: "

        letters = Set(tiles)
        words = []
        for s in sowpods:
            word = Set(s)
            canMakeWord = True
            if len(s) > len(tiles):
                continue
            else:
                for l in letters:
                    if s.count(l) > tiles.count(l):
                        canMakeWord = False
                
            if canMakeWord and word.issubset(letters) and s != "":
                words.append(s)

        words.sort(lambda x,y: cmp(len(y), len(x)))

        if len(words) == 0:
            speech += "no words"
        elif len(words) == 1:
            speech += words[0]
        else:
            speech += words[0]
            for w in words[1:-1]:
                speech += ", " + w
            speech += " and " + words[-1]

        say(speech + ".")


    def run(self):
        text = ""
        while text.lower() != "exit":
            say("What do you want to do?")
            text = raw_input()
            if text.lower().startswith("check"):
                self.checkDictionary(text[6:].lower())
            elif text.lower().startswith("make"):
                self.makeWords(text[5:].lower())

        say("Goodbye.")   

sh = ScrabbleHelper()
sh.run()
