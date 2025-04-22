from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        running_sum = 0
        current = 0

        for arrival, prep_time in customers:
            total_time = prep_time + arrival
            if current > arrival:
                diff = current - arrival
                total_time += diff
            current = total_time
            running_sum += total_time - arrival

        return running_sum / len(customers)
