from typing import List
from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                result -= 1
                count[sandwich] -= 1
            else:
                return result
        
        return result