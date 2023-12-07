class NumArray:
    def __init__(self, nums: list[int]):
        self.sum_range = []
        count = 0
        for num in nums:
            count += num
            self.sum_range.append(count)
        

    def sumRange(self, left: int, right: int) -> int:
        rightNum = self.sum_range[right]
        leftNum = self.sum_range[left - 1] if left > 0 else 0
        return rightNum - leftNum