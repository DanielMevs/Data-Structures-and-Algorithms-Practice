# - Time: O(n)
# - Space: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(s)
        left = 0
        for right in range(len(sList)):
            if sList[right] == ' ':
                temp = right - 1
                while left < temp:
                    sList[left], sList[temp] = sList[temp], sList[left]
                    temp, left = temp - 1, left + 1
                left = right + 1
        while left < right:
            sList[left], sList[right] = sList[right], sList[left]
            left, right = left + 1, right - 1
        
        return ''.join(sList)
    
