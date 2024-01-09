class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        currentLine, currentLineLength = [], 0
        i = 0

        while i < len(words):
            if currentLineLength + len(currentLine) + len(words[i]) > maxWidth:
                # - Line complete
                extra_space = maxWidth - currentLineLength
                spaces = extra_space // max(1, len(currentLine) - 1)
                remainder = extra_space % max(1, len(currentLine) - 1)
                
                for j in range(max(1, len(currentLine) - 1)):
                    currentLine[j] += " " * spaces
                    if remainder:
                        currentLine[j] += " "
                        remainder -= 1
                
                result.append(''.join(currentLine))

                # - Reset line and length
                currentLine, currentLineLength = [], 0

                

            currentLine.append(words[i])
            currentLineLength += len(words[i])
            i += 1
        
        # - Handling the last line
        last_line = ' '.join(currentLine)
        trailing_space = maxWidth - len(last_line)
        last_line += ' ' * trailing_space
        result.append(last_line)
        
        return result