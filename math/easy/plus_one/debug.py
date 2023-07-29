class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        is_placed = False
        carry = 1

        if i == 0:
            return [1] + [0] if digits[0] == 9 else [digits[0] + 1]
        
        while i >= 0:
            if digits[i] == 9 and not is_placed:
                digits[i] = 0
                print('a')
                
            elif digits[i] != 9 and not is_placed:
                carry = 1
                is_placed = True
                digits[i] = digits[i] + carry
                print('b')
            
            elif digits[i] == 9 and is_placed:
                carry = 0
                digits[i] = digits[i] + carry
                print('c')

            else:
                carry = 0
                digits[i] = digits[i] + carry
                print('d')

            i -= 1


        if not is_placed:
            digits = [carry] + digits

        return digits

print(Solution().plusOne([1,9]))