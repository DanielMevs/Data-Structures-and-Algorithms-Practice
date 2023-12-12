class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""
        for word in strs:
            result += str(len(word)) + "^" + word
        
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result, i = [], 0
        while i < len(str):
            j = i
            while str[j] != '^':
                j += 1
            length = int(str[i:j])
            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return result
    
# strs = ['apple', 'banana', 'kiwi', 'mango', 'blueberry']
# obj = Solution()
# encode_res = obj.encode(strs)
# print(f'type of encode result: {type(encode_res)}')
# print(f'encode result: {encode_res}')
# print('-' * 20)
# decode_res = obj.decode(encode_res)
# print(f'type of decode result: {type(decode_res)}')
# print(f'decode result: {decode_res}')
