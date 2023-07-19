class Solution:
    def hIndex(self, citations: list[int]) -> int:
        num_of_papers = len(citations)
        h_dict = {}
        for i, num in enumerate(citations):
            if num in h_dict.keys() or num == 0:
                continue
            end_range = (num_of_papers + i) 
            print(f'end_range {end_range}')
            for j in range(i, end_range):
                current_num_idx = j % num_of_papers
                print(f'current_num_idx: {current_num_idx}')
                if num not in h_dict.keys():
                    h_dict[num] = h_dict.get(num, 0) + num
                if citations[current_num_idx] >= num and j != i:
                    h_dict[num] = h_dict.get(num, 0) + num
                    print(f'num: {num}')
                    print(f'h_dict[num]: {h_dict[num]}')
                    print('-'*20)
        print(f'final dict: {str(h_dict)}')
        hindex = max(h_dict, key=h_dict.get)
        print(hindex)
        return hindex
    
Solution().hIndex([3,0,6,1,5])