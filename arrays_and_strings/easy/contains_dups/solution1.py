class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dummy = set()
        for num in nums:
            if num not in dummy:
                dummy.add(num)
            else:
                return True
        return False