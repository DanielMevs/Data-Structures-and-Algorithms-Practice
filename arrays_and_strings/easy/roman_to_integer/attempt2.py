class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        val = 0
        val_to_add = 0
        minor_count = 0
        for i, rom_char in enumerate(s):
            
            if symbol_dict[s[i]] > symbol_dict[s[i - 1]]:
                offset = 0
                minor_count = i - 1
                repeating_char = s[minor_count]
                while s[minor_count] == repeating_char:
                    offset += 1
                    val -= symbol_dict[s[minor_count]]
                    minor_count -= 1
                val_to_add = symbol_dict[s[i]] - (symbol_dict[repeating_char] * offset)
                val += val_to_add
            else:
                val += symbol_dict[rom_char]

        return val