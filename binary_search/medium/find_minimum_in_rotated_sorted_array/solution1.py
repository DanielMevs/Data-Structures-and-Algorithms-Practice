class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) -1 

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right) // 2
            result = min(result, nums[middle])
            # - Move our pointer to search the right sorted portion, where we 
            # know the values are less than those in the left sorted portion
            if nums[middle] >= nums[left]:
                left = middle + 1
            # - Else, we search the left sorted portion
            else:
                right = middle - 1
        
        return result
    

'''
input = [5, 1, 2, 3, 4]
result = 5; left = 0; right = 4
middle = 2; result = 2; 2 >= 5? ❌ -> right = 1
middle = 1 // 2 = 0; result = min(2, 5) = 5; 5 >= 5? ✅ -> left = 1
middle = 2 // 2 = 1; result = min(2, 1) = 1; 1 >= 1? ✅ -> left = 2
left > right? ✅ -> break;
return 1

'''