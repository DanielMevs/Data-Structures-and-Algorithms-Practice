class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        while t:
            print(f't[0]: {t[0]}')
            # if not s:
            #     break
            if t[0] in s:
                t = t[t.index(t[0]) + 1 :]
                s = s[:s.index(t[0])] + s[s.index(t[0]) + 1:]
            else:
                print(f's: {s}')
                return False
        if not t:
            return True
        
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))