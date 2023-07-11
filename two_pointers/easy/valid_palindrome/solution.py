class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        s = s.translate(str.maketrans(
            '','',string.punctuation
            )).lower().replace(' ', '')
        return s == s[::-1]
        