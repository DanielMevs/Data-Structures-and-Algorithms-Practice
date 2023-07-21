class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        while t:
            if t[0] in s:
                t = t[t.index(t[0]) + 1 :]
                s = s[:s.index(s[0])] + s[(s.index(s[0]) + 1) % len(s):]
            else:
                print(f's: {s}')
                print(f't: {t}')
                return False
        if not t:
            return True

s = 'ab'
t = 'ba'
print(Solution().isAnagram(s, t))