from typing import List
MOD = 1337


class Solution:
    
    def superPow(self, a: int, b: List[int]) -> int:
        a %= MOD
        result = 1
        for digit in b:
            result = (self.pow(result, 10) * self.pow(a, digit)) % MOD

        return result
    
    def pow(self, a: int, power: int) -> int:
        result = 1
        while power:
            if (power & 1):
                result = (result * a) % MOD
            a = (a * a) % MOD
            power >>= 1
        
        return result