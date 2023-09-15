class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)

        while left < right-1:
            if s[left] != s[right-1]:
                skipLeft, skipRight = s[left + 1: right], s[left:right-1]
                return (skipLeft == skipLeft[::-1]
                        or skipRight == skipRight[::-1])
            left, right = left + 1, right - 1
        
        return True