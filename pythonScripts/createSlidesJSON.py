import json

# script to parse the text file that the ai made
# and then convert it into a ppptx formmat

# read the text file into a string array
def textIntoLines(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if line == "\n" or len(line) == 0:
                continue
            lines.append(line[:line.index("\n")])
    return lines

# make the slides into tuples of format (slideNumber, title, bodyLines)
def linesIntoSlideObjects(lines):
    slides = {}
    index = 0
    while index < len(lines):
        # skip over the slide number
        index += 1
        if index >= len(lines):
            break
        
        # get the title of the current slide
        title = lines[index]

        # move to the body
        index += 1
        if index >= len(lines):
            break

        # get the body to the current slide
        bodyLines = []
        while True:
            # move on once the whole body was read
            if lines[index] == f"Slide {len(slides) + 2}:":
                break
            
            # add this line to the body
            bodyLines.append(lines[index])

            # move to the next body line
            index += 1
            if index >= len(lines):
                break

        # add this slide to the list  
        slides[str(len(slides) + 1)] = {"title": title, "body": bodyLines}
    return slides

with open("public/slideComponents/slidesObjects/slides.json", "w" ) as f:
    json.dump(linesIntoSlideObjects(textIntoLines("public/slideComponents/text/inputTxt.txt")), f, indent=4),