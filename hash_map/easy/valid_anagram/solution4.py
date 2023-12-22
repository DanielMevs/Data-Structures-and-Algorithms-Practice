class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_tracker, t_tracker = {}, {}

        for i in range(len(s)):
            s_tracker[s[i]] = s_tracker.get(s[i], 0) + 1
            t_tracker[t[i]] = t_tracker.get(t[i], 0) + 1
        
        return s_tracker == t_tracker