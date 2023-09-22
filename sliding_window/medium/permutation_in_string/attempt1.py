class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False
        
        s1_count = {char: s1.count(char) for char in s1}
        # print(s1_count)
        left_window, right_window = 0, len(s1)
        while right_window <= len(s2):
            sub_s2 = s2[left_window: right_window]
            s2_count = {char: sub_s2.count(char) for char in sub_s2}
            if s2_count == s1_count:
                return True
            else:
                left_window, right_window = left_window + 1, right_window + 1
            
            
        return False


Solution().checkInclusion(s1='abbc', s2='xqcbabips')
        