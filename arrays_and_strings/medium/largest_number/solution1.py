from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        print(f'nums: {nums}')
        print('-' * 20)
        
        def compare(n1, n2):
            print('-' * 20)
            print(f'n1: {n1}')
            print(f'n2: {n2}')
            print(f'n1 + n2: {n1 + n2 }')
            print(f'n2 + n1: {n2 + n1 }')
            if n1 + n2 > n2 + n1:
                print('case 1: -1')
                print('n1 + n2 > n2 + n1')
                return -1
            elif n1 < n2:
                print('case 2: 1')
                print('n1 < n2')
                return 1
            else:
                print('case 3: 0')
                print('n1 > n2')
                return 0
            print('-' * 20)

        nums = sorted(nums, key=cmp_to_key(compare))

        for num in nums:
            print(num)
            
        print('-' * 20)
        
        return str(int(''.join(nums)))
    
nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))