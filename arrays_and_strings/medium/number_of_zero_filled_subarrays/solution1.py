class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        conseq, result = 0, 0
        for num in nums: 
            if num == 0:
                conseq += 1
            else:
                conseq = 0
            
            result += conseq
        
        return result