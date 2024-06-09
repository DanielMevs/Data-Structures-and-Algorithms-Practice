class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            result = max(result, curMax)
            
        return result