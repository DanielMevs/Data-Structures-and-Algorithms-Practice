class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum_list = []
        nums.sort()
        for i in range(len(nums)):
            if (i > 0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                target = -1 * nums[i]
                while low < high:
                    if nums[low] + nums[high] == target:
                        three_sum_list.append([nums[i], nums[low], nums[high]])

                        # - Done to skip duplicates, high goes backwards
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                    elif nums[low] + nums[high] > target:
                        high -= 1
                    else:
                        low += 1
        return three_sum_list
                    