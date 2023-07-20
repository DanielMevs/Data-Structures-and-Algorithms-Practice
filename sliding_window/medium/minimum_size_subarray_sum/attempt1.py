class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        run_count = []
        temp_count = []
        for num in nums:
            if not temp_count:
                temp_count.append(num)
            else:
                temp_sum = sum(temp_count) + num
                if num >= target:
                    return 1

                    
                elif temp_sum < target:
                    temp_count.append(num)
                elif temp_sum >= target:
                    temp_count.append(num)
                    run_count.append(temp_count)
                    temp_count = []
                

        if not run_count:
            min_sub = 0
        elif len(run_count) == 1:
            return len(run_count[0])
        else:
            min_sub = len(min(run_count, key=len))
        
        return min_sub