def getElementsLeftOver(size, left):
    return size - left
    

def decode(message_file: str) -> str:
    lines = []
    result = ''
    left, right = 0, 1
    count = 1

    with open(message_file, 'r') as f:
        for line in f:
            lines.append(line.strip())

    sort_key = lambda x: int(x.split()[0])
    lines.sort(key=sort_key)

    
    while right <= len(lines):
        result += lines[right -1].split()[-1] + ' '
        left = right
        count += 1
        right += count 

    remaining = getElementsLeftOver(len(lines), left)
    if remaining:
        result += lines[left + remaining - 1]
    


    return result if remaining else result[:-1]


if __name__ == "__main__":
    print(decode('coding_qual_input.txt'))