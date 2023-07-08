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
        for i in range(min_word):

            prefix_tracker = []
            checker = lambda letter: letter == strs[0][i]
            for word in strs:
                prefix_tracker.append(checker(word[i]))
            if all(prefix_tracker):
                prefix += strs[i]
            else:
                break
        return prefix
            
        
        
        
        
f = Solution()
f.longestCommonPrefix(["reflower","flow","flight"])