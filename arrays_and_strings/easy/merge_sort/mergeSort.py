nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3

print(f'original nums1: {nums1}')
print(f'nums2: {nums2}')
print(f'n: {n}')
print(f'm: {m}')
print('_'*20+'\n')



def merge(nums1, m, nums2, n):
    i = 0

    for num in nums2:
        is_placed = False
        if m == 0:
            print('I am the man')
            nums1[i] = nums2[i]
            i += 1
            is_placed = True


            print(f'nums1: {nums1}')
            print(f'num: {num}')
            print(f'i: {i}')
            print('_'*20)
        
        elif n == 1:
            print('I am the knight')
            non_element_idx = nums1.index(0)
            if num < nums1[i]:
                print('I am red')
                print(f'nums1[i]: {nums1[i]}')
                temp = nums1[i]
                nums1[i] = num
                nums1[non_element_idx] = temp

                
            else:
                print('I am blue')
                print(f'nums1: {nums1}')
                print(f'i: {i}')
                if non_element_idx == len(nums1) - 1:
                    nums1[non_element_idx] = num
                    i -= 1
                    while nums1[i] < nums1[i-1]:
                        
                        temp = nums1[i - 1]
                        nums1[i - 1] = num
                        nums1[i] = temp 
                        i -= 1
                        print('I am turquoise')
                        print(f'nums1: {nums1}')
                        print(f'i: {i}')
                else:
                    nums1[non_element_idx] = num
                
            is_placed = True
            

        while not is_placed:
            if i == len(nums1) and not is_placed:
                print('I am here')
                if 0 not in nums1:
                    is_placed = True
                else:
                    non_element_idx = nums1.index(0)
                    print(non_element_idx)
                    nums1[non_element_idx:] = nums1[non_element_idx + 1:] 
                    nums1 += [num]
                    is_placed = True
                    

                print(f'nums1: {nums1}')
                print(f'num: {num}')
                print(f'i: {i}')
                print('_'*20)


            elif num > nums1[i]:
                if i > n:
                    print('I am tall')
                    if num > nums1[i] and n != m:
                        try:
                            nums1[i + 1:] = nums1[i: -1]
                            nums1[i+1] = num
                        except IndexError:
                            nums1[i] = num
                    else:
                        nums1[i] = num
                    
                    is_placed = True

                    print(f'nums1: {nums1}')
                    print(f'num: {num}')
                    print(f'i: {i}')
                    print('_'*20)
                    i += 1

                else:
                    print('I am there')
            
                    print(f'nums1: {nums1}')
                    print(f'num: {num}')
                    print(f'i: {i}')
                    print('_'*20)
                    i += 1


            elif num == nums1[i]:
                print('I am yonder')
                nums1[i + 1:] = nums1[i: -1]
                nums1[i] = num

                print(f'nums1: {nums1}')
                print(f'num: {num}')
                print(f'i: {i}')
                print('_'*20)
                is_placed = True


            elif num < nums1[i]:
                print('I am young')
                nums1[i + 1:] = nums1[i: -1]
                nums1[i] = num
                is_placed = True
                print(f'nums1: {nums1}')
                print(f'num: {num}')
                print(f'i: {i}')
                print('_'*20)

    print(nums1)


merge(nums1, m, nums2, n)
print(f'Expected output: {[1,2,2,3,5,6]}')