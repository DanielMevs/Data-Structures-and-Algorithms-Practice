class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        word_arr = s.split()
        for word in word_arr:
            for char in reversed(word):
                result += char
            result += ' '

        return result[:-1]
    