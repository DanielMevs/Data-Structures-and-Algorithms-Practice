class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and [i] != " ":
            length += 1
        
        return length