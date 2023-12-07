class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[i+1:]) == 0:
                    return i
            elif sum(nums[i::-1]) == sum(nums[i:]):
                return i
        return -1
