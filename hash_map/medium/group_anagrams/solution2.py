from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1
            
          
            res[tuple(count)].append(string)

        return res.values()
    
        