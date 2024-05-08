class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # - Base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)
            result.extend(perms)
            nums.append(num)
        
        return result