class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_list = s.split(' ')
        if len(pattern) != len(word_list):
            return False
        charMap, wordMap = {}, {}

        for i in range(len(word_list)):
            if pattern[i] in charMap.keys() and charMap[pattern[i]] != word_list[i]:
                return False
            else:
                 charMap[pattern[i]] = word_list[i]
            if word_list[i] in wordMap.keys() and wordMap[word_list[i]] != pattern[i]:
                return False
            else:
                 wordMap[word_list[i]] = pattern[i]
            
        return True