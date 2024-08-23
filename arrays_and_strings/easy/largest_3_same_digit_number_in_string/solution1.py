class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = "0"

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                result = max(result, num[i: i + 3])
        
        return "" if result == "0" else result