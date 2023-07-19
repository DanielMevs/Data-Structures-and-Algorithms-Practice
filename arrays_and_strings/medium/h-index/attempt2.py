class Solution:
    def hIndex(self, citations: list[int]) -> int:
        num_of_papers = len(citations)
        h_list = []
        for i, num in enumerate(citations):
            arr = [h for h in citations if h >= num]
            if len(arr) >= num:
                h_list.append(len(arr))
        print(h_list)
        arr2 = []
        for num in h_list:
            criterion2 = num_of_papers - num 
            arr3 = [paper for paper in citations if paper < num]
            if len(arr3) < num:
                arr2.append(num)
        print(max(arr3))
            

            # end_range = (num_of_papers + i) 
            # for j in range(i, end_range):
            #     current_num_idx = j % num_of_papers
            #     if num not in h_dict.keys():
            #         h_dict[num] = h_dict.get(num, 0) + num
            #     if citations[current_num_idx] >= num and j != i:
            #         h_dict[num] = h_dict.get(num, 0) + num
      
        # hindex = max(h_dict, key=h_dict.get)
        # print(hindex)
        # print(h_list)
        # hindex = max(h_list)
        # return hindex
    
# Solution().hIndex([3,0,6,1,5])
Solution().hIndex([1, 2, 4, 8, 9])