from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_num = max(arr1)
        all_nums = [0] * (max_num + 1)

        for num in arr1:
            all_nums[num] += 1

        result = []
        for num in arr2:
            result += [num] * all_nums[num]
            all_nums[num] = 0

        for num in range(len(all_nums)):
            result += [num] * all_nums[num]

        return result
