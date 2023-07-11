import string, timeit

def test_join(s: str) -> str:
    return ''.join(char for char in s if char != ' ')

def test_replace(s: str) -> str:
    return s.replace(' ', '')

s = "A man, a plan, a canal: Panama"

print("join      :",timeit.Timer('f(s)', 'from __main__ import s,test_join as f').timeit(1000000))
print("replace      :",timeit.Timer('f(s)', 'from __main__ import s,test_replace as f').timeit(1000000))
