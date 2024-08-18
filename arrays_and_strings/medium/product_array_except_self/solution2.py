from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postFix, preFix = [0] * len(nums), [0] * len(nums)
        result = []

        # - Populate the preFix array
        runSum = 1
        for i in range(len(nums)):
            preFix[i] = (runSum * nums[i])
            runSum = preFix[i]

        # - Populate the postFix array
        runSum = 1
        for i in range(len(nums) - 1, -1, -1):
            postFix[i] = (runSum * nums[i])
            runSum = postFix[i]

        # - Populate the result from the two arrays
        preFix = [1] + preFix
        postFix = postFix + [1]
        for i in range(len(nums)):
            result.append(preFix[i] * postFix[i+1]) 
        
        return result