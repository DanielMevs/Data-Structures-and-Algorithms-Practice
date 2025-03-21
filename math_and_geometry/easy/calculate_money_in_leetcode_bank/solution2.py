class Solution:
    # Key observation: each week differs by a constant value of 7
    def totalMoney(self, n: int) -> int:
        weeks = n // 7  # number of full weeks
        result = 0
        low = 28  # amount of money saved in first week
        high = 28 + 7 * (weeks - 1)  # amount of money saved in last week
        result = (weeks * (low + high) // 2)  # we can apply gaussian summation

        for i in range(n % 7):
            result += weeks + i + 1

        return result
