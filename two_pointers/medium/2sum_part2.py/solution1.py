class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            num_sum = numbers[i] + numbers[j]
            if num_sum > target:
                j -= 1
            elif num_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]
