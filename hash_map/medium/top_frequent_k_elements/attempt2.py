class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, numCount in count.items():
            freq[numCount].append(num)

        print(f'count: {count}')
        print(f'freq: {freq}')

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    print(result)
                    return result

Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)