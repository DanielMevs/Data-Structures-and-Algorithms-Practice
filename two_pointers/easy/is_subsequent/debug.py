s = "aaaaaa"
t = "bbaaaa"

for letter in t:
    if letter == s[0]:
        if len(s) > 1:
            s = s[1:]
        else:
            s = ''
    print(f'new s: {s}')

print(f's: {s}')
print(f's length: {len(s)}')

