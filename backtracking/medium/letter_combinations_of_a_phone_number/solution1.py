class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                result.append(currentStr)
                return
            
            for char in digitToChar[digits[i]]:
                backtrack(i+1, currentStr + char)

        if digits:
            backtrack(0, "")

        return result