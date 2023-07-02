class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = []
        for num in list(nums):
            if num not in unique_nums:
                unique_nums.append(num)
                print(f'num: {num}')
                print(f'unique nums: {unique_nums}')
            else:
                num_idx = nums.index(num)
                nums.pop(num_idx)
        k = len(unique_nums)
        print(f'Nums at the end: {nums}')
        return k
    
nums = [1,1,2]

remDup = Solution()
remDup.removeDuplicates(nums=nums)