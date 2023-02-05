from textAi import chatBot 
from dictMaker import dictMaker
from imageAi import clipArtBot
from pptxMaker import tiredStudent

import sys

if __name__ == "__main__": 
    key = "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"
    orginization = "org-QouCrr1mRGRGOAqomk5pcpqq"
    theme = sys.argv[1]
    
    # step one, create a text string from a chat ai
    textResponse = chatBot(key, orginization).getChatResponse(theme, 1024, 0.3)
    print(textResponse)
    
    # step two, make that text string into a more useful object format
    dictVersionOfData = dictMaker().createDict(textResponse)
    print(dictVersionOfData)

    # step three, generate the pictures
    imageBinarys = clipArtBot(key, orginization).createImages(dictVersionOfData)

    # step four, create the presentation
    tiredStudent(dictVersionOfData, imageBinarys).createPresentation()
