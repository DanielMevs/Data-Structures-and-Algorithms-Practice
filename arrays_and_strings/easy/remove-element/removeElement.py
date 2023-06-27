class Solution(object):

    # - Initialize the nums array and set val
    def __init__(self, nums, val) -> None:
        self.nums = nums
        self.val = val

    # - Function definition 
    def removeElement(self):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(self.nums):
            if self.nums[i] == self.val:
                while self.nums[i] == self.val:
                    print(f'num: {self.nums[i]}')
                    self.nums.pop(i)
                    print(f'i: {i}')
                    print('-'*20)
                    count += 1
                    i -= 1
                
                
                
                
            else:
                print(f'num: {self.nums[i]}')
                print(f'i: {i}')
                print('-'*20)
                i +=1
        return count


nums = [0,1,2,2,3,0,4,2]
val = 2
remEl = Solution(nums=nums,val=val)
print(f'original nums: {remEl.nums}')
remEl.removeElement()
print(f'list after call: {remEl.nums}')