from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        queue = deque()
        left = right = 0

        while right < len(nums):
            # -Pop values that are smaller than our current 
            #   number from the queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # - Remove left value from window
            if left > queue[0]:
                queue.popleft()
            
            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1
            
            right += 1
        
        return output