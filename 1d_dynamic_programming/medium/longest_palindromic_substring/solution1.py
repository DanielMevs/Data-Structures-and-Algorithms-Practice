class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resultLen = 0

        for i in range(len(s)):
            # - Check odd length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    result = s[left: right + 1]
                    resultLen = right - left + 1
                left -= 1
                right += 1
            
            # - Check even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    result = s[left: right + 1]
                    resultLen = right - left + 1
                left -= 1
                right += 1
        
        return result