class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        prefix_record = []
        
        
        
        for i in range(len(strs) - 1):
            if len(strs[i+1]) < len(strs[i]):
                sub_string = strs[i + 1]
                sup_string = strs[i]
                
            elif len(strs[i+1]) > len(strs[i]):
                sub_string = strs[i]
                sup_string = strs[i + 1]

                
            else:
                sub_string = strs[i]
                sup_string = strs[i+1]

            
            j = len(sub_string) - 1
            
            while j >= 0:
                if sub_string[:j] in sup_string:
                    if j == 0:
                        prefix_record.append(sub_string)
                    else:
                        start_idx = sup_string.find(sub_string[:j][0])
                        end_idx = sup_string.find(sub_string[:j][-1])
                        prefix_record.append(sup_string[start_idx: end_idx + 1])
                    break
                else:
                    
                    j -= 1
        print(prefix_record)
        return min(prefix_record, key=len) if prefix_record else ""
f = Solution()
f.longestCommonPrefix(["reflower","flow","flight"])