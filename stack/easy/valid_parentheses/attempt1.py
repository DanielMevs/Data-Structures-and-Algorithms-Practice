class Solution:
    def isValid(self, s: str) -> bool:
        closing_dict = {'}': '{', ')': '(', ']':'['}
        return