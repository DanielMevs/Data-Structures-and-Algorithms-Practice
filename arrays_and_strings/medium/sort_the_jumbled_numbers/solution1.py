from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []

        for idx, num in enumerate(nums):
            # Handle edge case when num == 0
            if num == 0:
                mapped_nums.append((mapping[0], idx))
                continue
            mult = 1
            total = 0

            while num > 0:
                remain = num % 10
                num //= 10
                total += mult * mapping[remain]
                mult *= 10
            mapped_nums.append((total, idx))

        return [
            nums[i] for _, i in sorted(mapped_nums, key=lambda x: (x[0], x[1]))
        ]
