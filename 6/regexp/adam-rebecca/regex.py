#!/usr/bin/python

import re

#opens up the text file
text = open("doctor_who_wiki.txt", "r")
tester = text.read()
text.close()

#uses the built-in dictionary
text2 = open("/usr/share/dict/words", "r")
words = text2.read()
dict = words.split("\n")
text2.close()

#gets all of the names out of the text file
def getNames( text ): 
    names = re.findall( r'[A-Z][a-z]* [A-Z][a-z]*|Mrs?. [A-Z][a-z]*|Dr. [A-Z][a-z]*' , tester)
    return names

#checks the first names against the dictionary
def checkNames( allNames ):
    result = []
    for name in allNames:
        if name not in dict: #only if they are not in the dictionary!
            result.append( name )
    return result

def checkDuplicates

if __name__ == "__main__":
    result = checkNames( getNames( tester ) )
    print result
