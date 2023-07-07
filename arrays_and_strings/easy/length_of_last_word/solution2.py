class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A tracker to handle the determination of finding
        #  non-white-space sequence's first occurence
        is_found = False
        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] ==' ' and is_found == False:
                i -= 1
            elif is_found == False and s[i] != ' ':
                count += 1
                i -= 1
                is_found = True
            elif is_found == True and s[i] != ' ':
                count += 1
                i -= 1
                
            else:
                break
            
            
        return count