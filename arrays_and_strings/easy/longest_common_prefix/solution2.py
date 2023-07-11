class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        min_word = min(strs, key=len)
        
        
        prefix = ''
        for i in range(len(min_word)):
            if all(word[i] == strs[0][i] for word in strs):
                prefix += strs[0][i]
            else:
                break
        return prefix