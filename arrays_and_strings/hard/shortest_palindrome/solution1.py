class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_pali(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        for r in reversed(range(len(s))):
            if is_pali(s, 0, r):
                suffix = s[r + 1:]
                return suffix[::-1] + s

        return ""
