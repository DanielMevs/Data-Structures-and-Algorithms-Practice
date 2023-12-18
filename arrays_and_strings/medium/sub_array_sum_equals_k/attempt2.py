# O(n^2)
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        temp = 0
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp += nums[j]
                if temp == k:
                    total += 1
            temp = 0
        
        return total