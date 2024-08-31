class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}  # char -> first index
        result = -1
        for i, char in enumerate(s):
            if char in char_index:
                result = max(result, i - char_index[char] - 1)
            else:
                char_index[char] = i
        
        return result