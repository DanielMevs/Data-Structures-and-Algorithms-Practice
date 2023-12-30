class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        left, right = 0, k
        unique_bins = set()

        while right <= len(s):
            unique_bins.add(s[left: right])
            left, right = left + 1, right + 1
            
        return len(unique_bins) >= 1 << k

        

print(Solution().hasAllCodes("00110110", 2))