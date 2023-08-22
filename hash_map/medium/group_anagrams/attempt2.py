from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # initializing a dictionary with lists are default values
        res = defaultdict(list)

        for string in strs:
            # to act as our key for our dictionary
            count = [0] * 26

            for char in string:
                # to map the char of a string to it's ASCI value
                count[ord(char) - ord("a")] += 1
            
            # print('tup: ' + str(tuple(count)))

            # we convert the list to a tuple to store it as our key 
            # lists cannot be keys because they are mutable
            # each tuple represents the asci value of each character in our string
            # each anagram will map to a unique configuration of these types of tuples
            res[tuple(count)].append(string)

        return res.values()
    
Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        