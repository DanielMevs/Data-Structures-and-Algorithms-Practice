class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        tracker = {}

        for i, num in enumerate(nums):
            
            tracker[num] =  [num]
            tracker = self.updateAdjacent(num, tracker)
        return max(tracker, key=len(tracker.values()))

    
    def updateAdjacent(target, tracker):
        for key, adjacents in tracker.items():
            if adjacents[0] == target + 1:
                adjacents = {key: [target] + adjacents}
                tracker.update(adjacents)
            elif adjacents[-1] == target - 1:
                adjacents = {key: adjacents + [target]}
                tracker.update(adjacents)
        return tracker