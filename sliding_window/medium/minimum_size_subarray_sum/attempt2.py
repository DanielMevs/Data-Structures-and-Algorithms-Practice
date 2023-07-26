class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_sub_size = 0
        left = 0
        right = 1
        

        while left < len(nums):
            sub_arr = []
            run_sum = 0
            while run_sum < target:
                sub_arr = nums[left:right]
                run_sum = sum(sub_arr)
                right += 1
            if len(sub_arr) < min_sub_size and len(sub_arr) != 0:
                min_sub_size = len(sub_arr)
            left += 1
            
        return len(sub_arr)
            
            
            
            