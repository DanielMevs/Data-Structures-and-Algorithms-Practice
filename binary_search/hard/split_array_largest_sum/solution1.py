# - O(nlog(S)) runtime where S = sum of nums

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            currentSum = 0
            for n in nums:
                currentSum += n
                if currentSum > largest:
                    subarray += 1
                    currentSum = n
            return subarray + 1 <= k
        
        left, right = max(nums), sum(nums)
        result = right

        while left <= right:
            mid = left + ((right - left) // 2)
            if canSplit(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result



