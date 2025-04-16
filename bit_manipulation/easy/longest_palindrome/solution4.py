class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = mask1 = mask2 = 0

        for c in s:
            if 'a' <= c <= 'z':
                bit = 1 << ord(c) - ord('a')
                if bit & mask1:
                    result += 2
                mask1 ^= bit
            else:
                bit = 1 << ord(c) - ord('A')
                if bit & mask2:
                    result += 2
                mask2 ^= bit

        return result + 1 if mask2 or mask1 else result
