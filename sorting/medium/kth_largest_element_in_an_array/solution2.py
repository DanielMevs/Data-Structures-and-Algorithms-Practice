# Quick select algorithm
# Worst time of O(n^2)
# Average time of O(n)


class Solution:
    def partition(self, nums: list[int], left: int, right: int) -> int:
        pivot, pointer = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1

        nums[pointer], nums[right] = nums[right], nums[pointer]

        return pointer

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]
