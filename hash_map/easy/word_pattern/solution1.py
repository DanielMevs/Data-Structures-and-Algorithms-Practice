class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_list = s.split(' ')
        if len(pattern) != len(word_list):
            return False
        charMap, wordMap = {}, {}

        for char, word in zip(pattern,word_list):
            if char in charMap and charMap[char] != word:
                return False
            else:
                 charMap[char] = word
            if word in wordMap and wordMap[word] != char:
                return False
            else:
                 wordMap[word] = char
            
        return True