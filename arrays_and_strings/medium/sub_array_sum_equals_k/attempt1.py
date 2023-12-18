class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        temp = 0
        total = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp == k:
                total += 1
                temp = nums[i]
            elif temp > k:
                temp = 0
            if nums[i] == k and i != 0:
                total += 1
        
        return total