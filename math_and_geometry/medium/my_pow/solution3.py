class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0:
                return 1
            elif (not n & 1):
                n >>= 1
                return helper(x * x, n)
            elif (n == 1):
                return x
            else:
                n >>= 1
                return x * helper(x * x, n)
        
        if n < 0:
            return helper(1 / x, -n)
        else:
            return helper(x, n)