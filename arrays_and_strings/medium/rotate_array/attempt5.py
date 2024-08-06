class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(len(nums)):
            nums[i] = [(i + k) % len(nums), nums[i]]
        
        for i in range(len(nums)):
            idx, val = nums[i][0], nums[i][1]
            nums[idx].append(val)
        
        for i in range(len(nums)):
            nums[i] = nums[i][-1]