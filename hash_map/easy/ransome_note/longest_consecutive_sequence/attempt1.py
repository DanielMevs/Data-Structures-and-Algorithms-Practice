from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_list = []
        for i, num in enumerate(nums):
            has_adjacent = [num2 for num2 in nums if num2==num+1 or num2==num-1].sort()
            has_adjacent = deque(has_adjacent)
            if not temp_list and has_adjacent:
                temp_list.append(deque(has_adjacent))
            for deq in [temp for temp in temp_list if temp != has_adjacent]:
                if deq[0] == has_adjacent[-1] + 1:
                    deq.appendleft(has_adjacent)
                elif deq[-1] == has_adjacent[0] - 1:
                    deq.appendright(has_adjacent)
                
                
            
