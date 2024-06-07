from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        right = 0
        for left in range(len(s2)):
            temp = count.copy()
            while right < len(s2) and \
                s2[right] in temp and \
                    temp[s2[right]] > 0:
                temp[s2[right]] -= 1
                right += 1
               
            if not any(temp.values()):
                return True
            right = left
            
        return False
    

# s1 = "adc"
# s2 = "dcda"
# print(Solution().checkInclusion(s1, s2))