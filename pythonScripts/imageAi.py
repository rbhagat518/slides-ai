import openai
import requests

# this class calls the Dalle Api with the title of the each slide
class clipArtBot():
    def __init__(self, key:str, orginization:str):
        openai.organization = orginization
        openai.api_key = key
    
    # returns the bytes of all the images for the slideshow
    def createImages(self, slideData:dict) -> list:
        images = []
        for i in range(1, len(slideData) + 1):
            if len(slideData[str(i)]["body"]) > 0:
                image_resp = openai.Image.create(prompt=slideData[str(i)]["title"], n=1, size="256x256")
                img_data = requests.get(image_resp["data"][0]["url"]).content
                images.append(img_data)
        return images