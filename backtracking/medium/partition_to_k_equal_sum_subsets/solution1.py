from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k:
            return False

        target = total_sum // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        memo = {}

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            if (tuple(used), k, subsetSum) in memo:
                return memo[(tuple(used), k, subsetSum)]

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False

            memo[(tuple(used), k, subsetSum)] = False
            return False

        return backtrack(0, k, 0)
