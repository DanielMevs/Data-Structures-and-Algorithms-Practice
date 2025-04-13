class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        stack = []
        words = sentence.split()

        for word in words:
            firstChar = word[0]
            if stack and stack.pop() != firstChar:
                return False
            stack.append(word[-1])

        return True if words[0][0] == words[-1][-1] else False
