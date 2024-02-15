class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        
        def isValid(threshold):
            i, count = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False
        
        if p == 0:
            return 0
        
        nums.sort()
        left, right = 0, 10**9
        result = 10 ** 9

        while left <= right:
            mid = left + (right - left) // 2
            if isValid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        