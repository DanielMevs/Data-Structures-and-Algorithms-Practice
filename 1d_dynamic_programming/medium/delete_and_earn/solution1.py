from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]]
            # Can't use both currEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(earn1 + currEarn, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = currEarn = earn2
                earn1 = temp

        return earn2
