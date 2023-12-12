from solution1 import Solution
from string import printable
from random import choice, randrange

# print(choice(printable))
# print(randrange(3, 9))

n = randrange(4,10)
test_arr = []
for i in range(n):
    test_str = ''
    str_len = randrange(4, 11)
    for j in range(str_len):
        test_str += choice(printable)
    test_arr.append(test_str)

print(f'Original test array: {test_arr}\n\n')
obj = Solution()
encode_test_str = obj.encode(test_arr)
print(f'Encoded result: {encode_test_str}')
print('-' * 20)
decode_test_arr = obj.decode(encode_test_str)
print(f'Decoded result: {decode_test_arr}')
print('-' * 20)
is_equal = 'Yes' if test_arr == decode_test_arr else 'No'
print(f'Decode is equal to original? -> {is_equal}')

