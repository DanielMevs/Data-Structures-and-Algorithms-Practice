# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(
            self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # find the peak
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # find target in the left side of the peak
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        # find target in the right side of the peak
        left, right = peak, length - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
