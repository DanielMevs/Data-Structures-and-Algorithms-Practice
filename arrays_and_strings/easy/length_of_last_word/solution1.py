class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return [len(seq) for seq in s.split(' ') if seq !=''][-1]