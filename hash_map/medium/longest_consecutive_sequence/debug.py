class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        tracker = {}

        for i, num in enumerate(nums):
            
            tracker[num] =  [num]
            tracker = self.updateAdjacent(num, tracker)
        lim = len(nums) - 1
        while lim > 0:
            num = nums[lim]
            tracker = self.updateAdjacent(num, tracker)
            lim -= 1

        max_seq = 0
        for adj_list in tracker.values():
            if len(adj_list) > max_seq:
                max_seq = len(adj_list)
        print(str(f'tracker: {tracker}'))
        return max_seq
    
    def updateAdjacent(self, target, tracker):
        for key, adjacents in tracker.items():
            if adjacents[0] == target + 1:
                adjacents = {key: [target] + adjacents}
                tracker.update(adjacents)
            elif adjacents[-1] == target - 1:
                adjacents = {key: adjacents + [target]}
                tracker.update(adjacents)
        return tracker
    
Solution().longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1])
