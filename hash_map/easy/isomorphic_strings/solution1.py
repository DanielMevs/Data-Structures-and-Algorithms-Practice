class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isoDictS = {}
        isoDictT = {}
        for i in range(len(s)):
            if t[i] in isoDictT.keys() and isoDictT[t[i]] != s[i]:
                return False
            else:
                isoDictT[t[i]] = s[i]
            if s[i] in isoDictS.keys() and isoDictS[s[i]] != t[i]:
                return False
            else:
                isoDictS[s[i]] = t[i]
        return True