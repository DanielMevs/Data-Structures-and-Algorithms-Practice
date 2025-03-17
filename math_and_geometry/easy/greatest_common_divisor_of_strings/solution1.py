class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(length):
            if len1 % length or len2 % length:
                return False
            factor1, factor2 = len1 // length, len2 // length
            return (
                str1[:length] * factor1 == str1 and
                str1[:length] * factor2 == str2
            )

        for length in range(min(len1, len2), 0, -1):
            if isDivisor(length):
                return str1[:length]

        return ""
