class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def sortWord(word):
            return ''.join(sorted(word))
        charDict = {sortWord(word): [] for word in strs}
        for word in strs:
            charDict[sortWord(word)].append(word)
        
        return charDict.values()