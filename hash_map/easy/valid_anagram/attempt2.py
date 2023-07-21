class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        while t:
            print(f't[0]: {t[0]}')
            # if not s:
            #     break
            if t[0] in s:
                replace = t[0]
                t = self.shrink(t, replace)
                s = self.shrink(s, replace)
            else:
                print(f's: {s}')
                return False
        if not t:
            return True
    
    def shrink(self, st, to_replace):
        return st.replace(to_replace, '', 1)
        
s = "anagram"
t = "nagaram"
# s = 'ab'
# t = 'ba'
print(Solution().isAnagram(s, t))