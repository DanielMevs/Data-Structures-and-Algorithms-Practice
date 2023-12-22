class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        for letter in t:
            if s:
                if letter == s[0]:
                    if len(s) > 1:
                        s = s[1:]
                    else:
                        s = ''
        return True if not s else False