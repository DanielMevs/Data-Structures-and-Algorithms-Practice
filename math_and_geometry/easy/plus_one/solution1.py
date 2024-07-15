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
                
                
            elif digits[i] != 9 and not is_placed:
                carry = 1
                is_placed = True
                digits[i] = digits[i] + carry
                
            
            elif digits[i] == 9 and is_placed:
                carry = 0
                digits[i] = digits[i] + carry
                
            else:
                carry = 0
                digits[i] = digits[i] + carry
                

            i -= 1


        if not is_placed:
            digits = [carry] + digits

        return digits

