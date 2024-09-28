class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        carry, result = 0, []

        a = a.zfill(maxLen)
        b = b.zfill(maxLen)

        for i in range(maxLen - 1, -1, -1):
            bitSum = carry
            bitSum += int(a[i])
            bitSum += int(b[i])

            result.append(str(bitSum % 2))
            carry = bitSum // 2
        
        if carry:
            result.append('1')

        result.reverse()

        return ''.join(result)

        