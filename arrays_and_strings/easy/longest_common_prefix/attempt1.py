class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        comparator = strs[0]
        prefix = ''
        shortest_word = comparator
        if len(strs) > 1:
            for i in range(1, len(strs)):
                if len(strs[i]) < len(shortest_word):
                    shortest_word = strs[i]
                for j in range(len(shortest_word)):
                    
                    if strs[i][j] == comparator[j] and strs[i][j] not in prefix:
                        prefix += strs[i][j]
                        
                    else:
                        break
            if prefix:
                return prefix
            else:
                return ""
        else:
            return comparator
        

