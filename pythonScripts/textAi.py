import openai
openai.organization = "org-QouCrr1mRGRGOAqomk5pcpqq"
openai.api_key = "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"

# create a completion
completion = openai.Completion.create(engine="text-davinci-003", prompt="Write me a slideshow on hackathons",max_tokens=512,temperature = 0)
# write it to the text file
with open("public/slideComponents/text/inputTxt.txt", "w") as f:
    f.write(completion.choices[0].text + "\n")