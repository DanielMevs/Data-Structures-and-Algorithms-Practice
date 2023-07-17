class Solution:
    def hIndex(self, citations: list[int]) -> int:
        num_of_papers = len(citations)
        h_dict = {}
        for i, num in enumerate(citations):
            for j in range(i, num_of_papers + i):
                if citations[j % num_of_papers] >= num:
                    h_dict[num] = h_dict.get(num, 0) + num
        return max(h_dict)
