class Solution:
    def partitionString(self, s: str) -> int:
        result, temp = 1, set()
        
        for letter in s:
            if letter in temp:
                result += 1
                temp = set()

            temp.add(letter)      

        return result