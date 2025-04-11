from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = set()

        for num in nums:
            if num not in count:
                count.add(num)
            else:
                count.remove(num)

        return not count
