class Solution:    
    def isSubsequence(self, s: str, t: str) -> bool:
            result = list(s)
            for i in range(len(t) - 1, -1, -1):
                if result and result[-1] == t[i]:
                    result.pop()
            
            return False if result else True