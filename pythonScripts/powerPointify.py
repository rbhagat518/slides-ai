from textAi import chatBot 
from dictMaker import dictMaker
from imageAi import clipArtBot
from pptxMaker import tiredStudent

import sys

# this main script handles all steps of slide creation
if __name__ == "__main__": 

    # read api key and orginization from a text file
    with open("keyFile.txt", "r") as f:
        key = f.readline().replace("\n", "")
        orginization = f.readline().replace("\n", "")

    # theme sent in from arguments
    theme = sys.argv[1]
    
    # step one, create a text string from a chat ai
    textResponse = chatBot(key, orginization).getChatResponse(theme, 1024, 0)
    
    # step two, make that text string into a more useful object format
    dictVersionOfData = dictMaker().createDict(textResponse)

    # step three, generate the pictures
    imageBinarys = clipArtBot(key, orginization).createImages(dictVersionOfData)

    # step four, create the presentation
    tiredStudent(dictVersionOfData, imageBinarys).createPresentation()