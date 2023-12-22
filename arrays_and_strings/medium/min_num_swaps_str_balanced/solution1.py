class Solution:
    def minSwaps(self, s: str) -> int:
        close_count, max_close = 0, 0

        for char in s:
            if char == '[':
                close_count -= 1
            else:
                close_count += 1
            max_close = max(close_count, max_close)
        
        return (max_close + 1) // 2