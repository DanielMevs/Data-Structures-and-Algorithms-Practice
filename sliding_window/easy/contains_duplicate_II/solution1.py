class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(nums):
            if abs(right - left) > k:
                window.remove(left)
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        
        return False