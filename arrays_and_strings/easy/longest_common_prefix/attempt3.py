class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''
        
        for i in range(len(strs) - 1):
            if strs[i] in strs[i + 1]:
                substring = strs[i]
                supstring = strs[i + 1]
                
            elif strs[i + 1] in strs[i]:
                substring = strs[i + 1]
                supstring = strs[i]
                
            else:
                continue

            substr_start = supstring.find(substring)
            j = substr_start
            while supstring[substr_start: j] in substring:
                if j - substr_start >= len(substring):
                    j += 1
                else:
                    prefix += supstring[j]
                    j += 1
        
        return prefix

        

