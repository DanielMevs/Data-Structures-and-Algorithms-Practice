class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        visited = set()
        runSum, left = 0, 0

        for char in s:
            if char not in visited:
                runSum += 1
                result = max(result, runSum)
                visited.add(char)
            else:
                while s[left] != char:
                    visited.remove(s[left])
                    left += 1
                    runSum -= 1
                
                left += 1
                
        return result
        