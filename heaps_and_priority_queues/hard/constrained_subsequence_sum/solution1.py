from typing import List
from heapq import heappop, heappush


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        result = nums[0]
        max_heap = [(-nums[0], 0)]  # max_sum, index

        for i in range(1, len(nums)):
            while i - max_heap[0][1] > k:
                heappop(max_heap)
            curr_max = max(nums[i], nums[i] - max_heap[0][0])
            result = max(result, curr_max)
            heappush(max_heap, (-curr_max, i))

        return result
