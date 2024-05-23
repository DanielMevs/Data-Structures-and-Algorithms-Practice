class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        closing_dict = {'}': '{', ')': '(', ']': '['}
        
        for char in s:
            if char in closing_dict:
                if charStack and charStack[-1] == closing_dict[char]:
                    charStack.pop()
                else:
                    return False
            else:
                charStack.append(char)
        return True if not charStack else False