from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums = nums[::-1]
        nums = nums[:k][::-1] + nums[k:][::-1]