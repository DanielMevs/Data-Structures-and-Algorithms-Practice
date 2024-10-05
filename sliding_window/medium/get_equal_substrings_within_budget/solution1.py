class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0, 0
        cost = 0
        result = 0

        while right < len(s):
            cost += abs(ord(s[right]) - ord(t[right]))
            right += 1

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            result = max(result, right - left)

        return result
    