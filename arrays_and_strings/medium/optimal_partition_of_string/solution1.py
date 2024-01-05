class Solution:
    def partitionString(self, s: str) -> int:
        result, temp = 0, set()
        
        for letter in s:
            if letter in temp:
                result += 1
                temp = set()
                temp.add(letter)
            else:
                temp.add(letter)        

        return result + 1