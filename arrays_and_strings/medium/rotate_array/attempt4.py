class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
        
        return nums