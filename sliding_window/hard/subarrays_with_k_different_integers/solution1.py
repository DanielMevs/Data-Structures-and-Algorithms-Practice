from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        leftNear, leftFar = 0, 0
        right = 0
        result = 0
        count = defaultdict(int)

        while right < len(nums):
            count[nums[right]] += 1
       
            while len(count) > k:
                count[nums[leftNear]] -= 1
                if count[nums[leftNear]] == 0:
                    count.pop(nums[leftNear])
                leftNear += 1
                leftFar = leftNear

            while count[nums[leftNear]] > 1:
                count[nums[leftNear]] -= 1
                leftNear += 1

            if len(count) == k:
                result += (leftNear - leftFar) + 1
                     
            right += 1
        
        return result
    