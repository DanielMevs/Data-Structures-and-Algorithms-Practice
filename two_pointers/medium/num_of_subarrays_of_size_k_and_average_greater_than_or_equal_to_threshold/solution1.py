class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        result = 0
        # - The sum of the subarray upto, but no including, the kth index element
        currentSum = sum(arr[:k-1])
        
        for left in range(len(arr) - k + 1):
            currentSum += arr[left + k - 1]
            if (currentSum / k) >= threshold:
                result += 1
            currentSum -= arr[left]
        
        return result
