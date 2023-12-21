from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        left = set()
        right = Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                char = chr(ord('a') + j)
                if char in left and char in right:
                    result.add((s[i], char))
        
            left.add(s[i])
        
        return len(result)

