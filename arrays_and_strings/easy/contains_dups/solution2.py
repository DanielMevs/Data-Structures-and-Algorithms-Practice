class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if nums_dict[num] > 1:
                return True
        return False