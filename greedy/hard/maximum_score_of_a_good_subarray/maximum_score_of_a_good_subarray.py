from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        result = nums[k]
        current_min = nums[k]

        while left > 0 or right < len(nums) - 1:
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1

            current_min = min(current_min, nums[left], nums[right])
            result = max(result, current_min * (right - left + 1))

        return result
