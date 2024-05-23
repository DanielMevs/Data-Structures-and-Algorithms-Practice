class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramDict = {}
        for i in range(len(strs)):
            word = self.helper(strs[i])
            if word not in anagramDict:
                anagramDict[word] = [i]
            else:
                anagramDict[word] += [i]
        anagramList = []

        for val in anagramDict.values():
            temp = []
            for idx in val:
                temp.append(strs[idx])
            anagramList.append(temp)

        return anagramList

    def helper(self, word: str) -> str:
        return ''.join(sorted(word))
        