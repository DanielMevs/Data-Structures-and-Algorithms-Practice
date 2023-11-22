# - Runs in O(nlog(n))

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def mergeSort(arr, left, right):
            # - The base case, which is the size of the arr equals 1
            if left == right:
                return arr
            # - Get the middle of the array as a dividing point
            middle = (left + right) // 2
            # - Merge the left half first
            mergeSort(arr, left, middle)
            # - Merge the right half next
            mergeSort(arr, middle + 1, right)
            merge(arr, left, middle, right)
            return arr

        def merge(arr, left_pointer, middle, right):
            left, right = arr[left_pointer: middle + 1], arr[middle + 1: right + 1]
            # - i is the pointer to our original array
            # - j is the pointer to our left sub-array
            # - k is the pointer to our right sub-array
            i, j, k = left_pointer, 0, 0

            # - Determine what value in the left sub-array and right sub-array is the least
            # and merge that value into our original array
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            # - To account for the scenario where we've used up all the elements in the right sub-array
            # but there are still elements left over in the left sub-array
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            # - To account for the scenario where we've used up all the elements in the left sub-array
            # but there are still elements left over in the right sub-array
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        return mergeSort(nums, 0, len(nums) - 1)