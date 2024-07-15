class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        inc = (numRows - 1) * 2

        for i in range(numRows):           
            j = i
            result += s[j]
            while j < len(s):
                if (i != 0 and i != numRows - 1) and (
                    j + (inc - (2 * i))) < len(s):
                    result += s[(j + (inc - (2 * i)))]
                j += inc 
                if j < len(s):
                    result += s[j]
        
        return result
