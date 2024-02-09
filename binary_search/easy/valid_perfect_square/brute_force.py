# O(√n) runtime

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        current = 1
        while True:
            if current * current == num:
                return True
            elif current * current > num:
                return False
            else:
                current += 1
    
    
