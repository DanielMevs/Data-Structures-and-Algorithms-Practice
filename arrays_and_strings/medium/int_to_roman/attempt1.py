class Solution:
    def intToRoman(self, num: int) -> str:
        charDict = {
            range(1, 4): ('I', 1),
            range(4, 5): ('IV', 4),
            range(5, 9): ('V', 5),
            range(9, 10): ('IX', 9),
            range(10, 40): ('X', 10),
            range(40, 50): ('XL', 40),
            range(50, 90): ('L', 50),
            range(90, 100): ('XC', 90),
            range(100, 400): ('C', 100),
            range(400, 500): ('CD', 400),
            range(500, 900): ('D', 500),
            range(900, 1000): ('CM', 900),
            range(1000, 4000): ('M', 1000)  
        }

        def get_roman_and_decr(numKey):
            if numKey == 0:
                return ('', 0)
            for numRange in charDict.keys():
                # print('*'*29)
                # print(numRange)
                # print(numKey)
                if numKey in numRange:
                    return charDict[numRange]

        def get_num_length(val):
            count = 0
            while val:
                val //= 10
                count += 1
            return count

        def get_roman_numeral(keyNum, decimalPlace):
            result = ''
            sigFig = keyNum * (10**decimalPlace)
            while sigFig > 0:
                
                romanChar, decr = get_roman_and_decr(sigFig)
                result += romanChar
                sigFig -= decr
                print(f'sig fig: {sigFig}')
                
            return result

        result = ''
        for i in range(get_num_length(num) - 1, - 1, -1):
            result += get_roman_numeral(num//(10**i), i)
            print(f'result: {result}')
            print(f'num before decr: {num}')
            num -= ((num // (10**i)) * (10**i))
            print(f'num: {num}')
        
        return result


expected = 'MMMDCCXLIX'
actual = Solution().intToRoman(num=3749)

print(f'result: {actual}')
assert actual == expected