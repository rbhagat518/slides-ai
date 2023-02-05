from textAi import chatBot 
from dictMaker import dictMaker
from imageAi import clipArtBot
from pptxMaker import tiredStudent

import sys

if __name__ == "__main__": 
    key = "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"
    orginization = "org-QouCrr1mRGRGOAqomk5pcpqq"
    theme = sys.argv[1]
    # theme = "bugs"
    
    # step one, create a text string from a chat ai
    textResponse = chatBot(key, orginization).getChatResponse(theme, 1024, 0)
    print(textResponse)
    
    # step two, make that text string into a more useful object format
    dictVersionOfData = dictMaker().createDict(textResponse)
    print(dictVersionOfData)

    # step three, generate the pictures
    imageBinarys = clipArtBot(key, orginization).createImages(dictVersionOfData)

    # step four, create the presentation
    tiredStudent(dictVersionOfData, imageBinarys).createPresentation()
