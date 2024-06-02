# Given stairs with n steps, how many ways can we get 
# to the last step if we are allowed to
# take 1 or 2 steps at a time.

class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one