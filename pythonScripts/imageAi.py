import openai
import requests
import json
openai.organization = "org-QouCrr1mRGRGOAqomk5pcpqq"
openai.api_key = "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"

with open("public/slideComponents/slidesObjects/slides.json", "w" ) as f:
    slides = json.load(f)

for i in range(1, len(slides)):
    image_resp = openai.Image.create(prompt=slides[str(i)]["title"], n=1, size="256x256")
    img_data = requests.get(image_resp["data"][0]["url"]).content
    with open("image" + str(i) + ".png", "wb") as h:
        h.write(img_data)