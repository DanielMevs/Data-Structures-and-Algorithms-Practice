class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_count = {}
        for i in range(n):
            if nums[i] not in num_count.keys():
                num_count.setdefault(nums[i], 0)
            num_count[nums[i]] = num_count.get(nums[i]) + 1
        return max(num_count, key=num_count.get)