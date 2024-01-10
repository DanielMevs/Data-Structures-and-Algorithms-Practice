from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        # - Map first char of each word to a set of suffixes
        wordMap = defaultdict(set)
        result = 0

        for word in ideas:
            wordMap[word[0]].add(word[1:])

        for char1 in wordMap:
            for char2 in wordMap:
                if char1 == char2:
                    continue
                duplicates = 0
                for word in wordMap[char1]:
                    if word in wordMap[char2]:
                        duplicates += 1
                distinct1 = len(wordMap[char1]) - duplicates
                distinct2 = len(wordMap[char2]) - duplicates
                result += distinct1 * distinct2
        
        return result

                
