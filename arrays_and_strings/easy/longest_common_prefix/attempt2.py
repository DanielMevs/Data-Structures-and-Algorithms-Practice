class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        end_prefix_idx = 0
        prefix = ''
        for i in range(1, len(strs)):
            prefix_found = False
            j = 0
            prefix_found = True
            while j < len(strs[i]) and j < len(strs[i-1]) and prefix_found:
                if strs[i][j] == strs[i - 1][j]:
                    prefix += strs[i][j]
                    j += 1
                    
                elif strs[i][j] != strs[i - 1][j] and prefix_found:
                    prefix = prefix[:j]
                    prefix_found = False
                    j += 1
                else:
                    j += 1
        return prefix

        

