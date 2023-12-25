class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        out = ''.join(str(num) for num in nums)
    

        return ''.join(sorted(out, key=lambda x: ord(x), reverse=True))