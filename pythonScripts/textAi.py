import openai

class chatBot():
    def __init__(self, key:str, orginization:str):
        openai.organization = orginization
        openai.api_key = key

    def getChatResponse(self, theme: str, tokens: int, temp: float) -> str:
        # one = "Write me a slideshow on " + theme + " that is 3 to 5 slides long, with the following output format.\n"
        # two = "SlideNumber:\nSlideTitle\nSlideBody\n"
        # three = "SlideNumber will be the slides number followed by a newline character, SlideTitle will be its title followed by a newline char,"
        # four = "and SlideBody will be a combination of 3 to 5 sentences and or bullet points each followed by newline characters.\n"
        # five = "The first slide will be a title slide and will only have a SlideNumber and a SlideTitle, it will not have a SlideBody"
        # userPrompt = one + two + three + four + five
        userPrompt= f"write me a slideshow on {theme}. (it must consist of 3-5 slides)\n\"\nHere is an example of the output format:\n\nSlide number # (write \"Slide (Number):\", always followed by 2 new line character) \n\nTitle (simply write the title, always followed by 1 new line character)\n\nBody (have a moderate amount of bullets and complete sentences within the slideshow, simply write the body)\n\n\""
        text = openai.Completion.create(engine="text-davinci-003", prompt=userPrompt, max_tokens=tokens, temperature=temp, top_p=1, frequency_penalty=0, presence_penalty=0).choices[0].text + "\n"
        text = text.replace("Title:", "").replace("Body:", "")
        return text