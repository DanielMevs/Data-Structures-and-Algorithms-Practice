# - Ask: print the input number in reverse
# order without casting it to a string.

def reverse_num(num: int) -> int:

    result = 0
    multiplier = 1
    length, stack = get_length_and_stack(num)

    for _ in range(length):
        num = stack.pop()
        result += (num * multiplier)
        multiplier *= 10

    return result



def get_length_and_stack(num: int) -> int:
    count = 0
    stack = []
    while num > 0:
        stack.append(num % 10)
        num = num // 10
        count += 1
        
    return count, stack

def main():
    num = 4567
    print(reverse_num(num=num))

if __name__ == '__main__':
    main()