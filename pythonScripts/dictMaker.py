class dictMaker():
    def createDict(self, text: str) -> dict:
        return self.__linesIntoDict(self.__textIntoLines(text))
    
    def __textIntoLines(self, text: str) -> list:
        lines = []
        textLines = text.splitlines(True)
        for line in textLines:
            if line == "\n" or len(line) == 0:
                continue
            lines.append(line[:line.index("\n")])
        return lines
    
    def __linesIntoDict(self, lines: list) -> dict:
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