class Solution:
    def isHappy(self, n: int) -> bool:
        
        tracker = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in tracker:
                return False
            tracker.add(n)

        return True