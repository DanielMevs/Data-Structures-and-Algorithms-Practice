class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum_list = []
        nums.sort()
        for i, num in enumerate(nums):
            if (i > 0 and num != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                
                while low < high:
                    three_sum = num + nums[low] + nums[high]
                    if three_sum == 0: 
                        three_sum_list.append([nums[i], nums[low], nums[high]])

                        # - Done to skip duplicates, high goes backwards
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        
                    elif three_sum > 0:
                        high -= 1
                    else:
                        low += 1
        return three_sum_list
                    