class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        k = len(nums)
        slow, fast, i = 0, 1, 1
        while fast < len(nums):
            while fast < len(nums) and nums[slow] == nums[fast]:
                k -= 1
                fast += 1
            nums[i] = nums[fast] if fast < len(nums) else nums[i]
            i += 1
            slow = fast
            fast += 1
        
        return k