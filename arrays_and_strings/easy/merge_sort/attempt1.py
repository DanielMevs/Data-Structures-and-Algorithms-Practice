class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0

        for num in nums2:
            is_placed = False
            if m == 0:
                nums1[i] = nums2[i]
                i += 1
                is_placed = True
            elif n == 1:
                non_element_idx = nums1.index(0)
                if num < nums1[i]:
                    temp = nums1[i]
                    nums1[i] = num
                    nums1[non_element_idx] = temp
                else:
                    if non_element_idx == len(nums1) - 1:
                        nums1[non_element_idx] = num
                        i -= 1
                        while nums1[i] < nums1[i-1]:
                            
                            temp = nums1[i - 1]
                            nums1[i - 1] = num
                            nums1[i] = temp 
                            i -= 1
                    else:
                        nums1[non_element_idx] = num
                is_placed = True

            while not is_placed:
                if i == len(nums1) and not is_placed:
                    if 0 not in nums1:
                        is_placed = True
                    else:
                        non_element_idx = nums1.index(0)
                        nums1[non_element_idx:] = nums1[non_element_idx + 1:]
                        nums1 += [num]
                        is_placed = True


                elif num > nums1[i]:
                    if i > n:
                        # nums1[i] = num
                        if num > nums1[i] and n != m:
                            try:
                                j = i
                                if nums1[i] == nums1[i + 1] and nums1[i] != 0:
                                    nums1[i + 1:] = nums1[i: -1]
                                    nums1[i + 1] = num
                                    j += 1
                                    while nums1[j+1] < num and nums1[j+1] != 0:
                                        temp = nums1[j+1]
                                        nums1[j+1] = num
                                        nums1[j] = temp
                                        j += 1
                                else:
                                    nums1[i + 1:] = nums1[i: -1]
                                    
                                    nums1[i+1] = num
                                    j -= 1
                                    while nums1[j - 1] > num and nums1[j-1] != 0:
                                        temp = nums1[j - 1]
                                        nums1[j - 1] = num
                                        nums1[j] = temp
                                        j -= 1
                                

                            except IndexError:
                                nums1[i] = num
                        else:
                            nums1[i] = num
                        is_placed = True
                        i += 1


                    else:
                        i += 1


                elif num == nums1[i]:
                    nums1[i + 1:] = nums1[i: -1]
                    nums1[i] = num


                    is_placed = True


                elif num < nums1[i]:
                    nums1[i + 1:] = nums1[i: -1]
                    nums1[i] = num
                    is_placed = True
