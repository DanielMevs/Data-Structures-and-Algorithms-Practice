class Solution(object):
    
    def longestCommonPrefix(self, strs):
        """Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        """
        result = ''

        for i in range(len(strs[0])):
            for st in strs:
                # - If i is equal to the length of a substring
                # we return because then we are not looking at 
                # common letters at that point.
                # - If the character of the current substring
                # no longer equals to the element of our first
                # string at that index, we no longer have 
                # letters in common so we return in that
                # case as well.
                if i == len(st) or st[i] != strs[0][i]:
                    return result
            # - If all the letters of each substring in our list for that
                # given index are equal, we add that character to result
            result += strs[0][i]
        
        return result