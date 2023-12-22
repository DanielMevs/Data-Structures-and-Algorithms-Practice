class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = [_ for _ in range(2*len(nums))]
        num_count = {}
        N = len(nums)
        for i in range(N):
            num_count[i] = nums[i]
        for i in range(len(result)):
            result[i] = num_count[i%N]
        
        return result