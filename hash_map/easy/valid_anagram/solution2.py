class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tracker = {}
        t_tracker = {}

        if len(s) > len(t):
            return False
        for i in range(len(s)):
            s_tracker[s[i]] = s_tracker.get(s[i], 0) + 1
        for j in range(len(t)):
            t_tracker[t[j]] = t_tracker.get(t[j], 0) + 1
        
        for t_char in t_tracker.keys():
            if t_char not in s_tracker.keys():
                return False
            elif s_tracker[t_char] != t_tracker[t_char]:
                return False
        return True
        


            
    
  
        
