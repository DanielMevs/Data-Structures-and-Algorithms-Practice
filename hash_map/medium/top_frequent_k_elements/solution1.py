class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        countDict = {}

        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1
        
        return sorted(countDict, key=lambda x: countDict[x], reverse=True)[:k]
    
        # - Alternatively:
        
        # return sorted(countDict, key=lambda x: countDict[x])[-k:]
            