class Solution:
    def canJump(self, nums: list[int]) -> bool:
        end = len(nums) - 1
        if end == 1:
            return True

        for i, num in enumerate(nums):
            print(f'i: {i}')
            print(f'num: {num}')
            print(f'i + num: {i + num}')
            print(f'end: {end}')
            if i + num == end:
                return True
        return False

print(Solution().canJump([2,3,1,1,4]))