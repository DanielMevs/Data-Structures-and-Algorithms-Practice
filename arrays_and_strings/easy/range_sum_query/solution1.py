class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum_count = []
        for i in range(len(self.nums)):
            if i == 0:
                sum_count.append(self.nums[i])
            else:
                sum_count.append(self.nums[i]+ sum_count[i -1])
        if left == 0:

            return sum_count[right] 
        else:
            return sum_count[right] - sum_count[left-1]