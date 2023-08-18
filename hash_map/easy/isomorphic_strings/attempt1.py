class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isoDictS = {}
        isoDictT = {}
        for i in range(len(s)):
            if t[i] in isoDictS.values():
                return False
            else:
                isoDictS[s[i]] = t[i]
            if s[i] in isoDictT.values():
                return False
            else:
                isoDictT[t[i]] = s[i]
        return True