# - O(log(min(n, m))) runtime

class Solution:
    def findMedianSortedArrays(
            self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2  # A pointer
            j = half - i - 2  # B pointer

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # - Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # - Odd
                if total % 2:
                    return min(Aright, Bright)
                # - Even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                right = i - 1
            
            else:
                left = i + 1

        