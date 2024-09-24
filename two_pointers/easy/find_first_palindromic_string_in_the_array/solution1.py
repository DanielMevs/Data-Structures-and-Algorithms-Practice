from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            left, right = 0, len(w) - 1
            while w[left] == w[right]:
                if left >= right:
                    return w
                left, right = left + 1, right - 1
        
        return ""