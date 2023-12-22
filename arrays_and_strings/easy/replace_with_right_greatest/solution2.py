class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        current_greatest = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr)-2, -1, -1):
            
            temp = current_greatest
            if arr[i] > current_greatest:
                current_greatest = arr[i]
            arr[i] = temp
            
            
        return arr
    
