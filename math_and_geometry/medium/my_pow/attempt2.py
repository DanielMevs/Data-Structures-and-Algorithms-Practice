class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 0:
            return 0
        
        return ((self.myPow(x**2) * (n % 2)*self.myPow(n//2), n//2))
