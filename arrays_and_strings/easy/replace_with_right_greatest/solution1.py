class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        greatestMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newGreatest = max(arr[i], greatestMax)
            arr[i] = greatestMax
            greatestMax = newGreatest
        
        return arr