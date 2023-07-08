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

            prefix_tracker = []
            checker = lambda letter: letter == strs[0][i]
            for word in strs:
                prefix_tracker.append(checker(word[i]))
            if all(prefix_tracker):
                prefix += strs[0][i]
            else:
                break
        return prefix
