class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        while t:

            if t[0] in s:
                replace = t[0]
                t = self.shrink(t, replace)
                s = self.shrink(s, replace)
            else:
                
                return False
        if not t:
            return True
    
    def shrink(self, st, to_replace):
        return st.replace(to_replace, '', 1)
        
