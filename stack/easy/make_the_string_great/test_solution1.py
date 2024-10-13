import timeit


class BadPairDetector:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
    
    def is_bad_pair(self):
        return abs(ord(self.char1) - ord(self.char2)) == 32
    
    def is_bad_pair_v2(self):
        return (
            self.char1 != self.char2 and
            self.char1.lower() == self.char2.lower()
        )
    
    def is_bad_pair_v3(self):
        def lower(char):
            if ord(char) < ord('a'):
                return chr(ord('a') + ord(char) - ord('A'))
            return char
        
        return self.char1 != self.char2 and self.char1 == lower(self.char2)
    

def main():
    badPairDetector = BadPairDetector('a', 'A')

    # Time the performance of the is_bad_pair method
    print(timeit.timeit(badPairDetector.is_bad_pair, number=1000000))
    print(timeit.timeit(badPairDetector.is_bad_pair_v2, number=1000000))
    print(timeit.timeit(badPairDetector.is_bad_pair_v3, number=1000000))
    print('---'*10)
    badPairDetector2 = BadPairDetector('a', 'b')

    # Time the performance of the is_bad_pair_v2 method
    print(timeit.timeit(badPairDetector2.is_bad_pair, number=1000000))
    print(timeit.timeit(badPairDetector2.is_bad_pair_v2, number=1000000))
    print(timeit.timeit(badPairDetector2.is_bad_pair_v3, number=1000000))
    print('---'*10)
    
    badPairDetector3 = BadPairDetector('A', 'a')
    print(timeit.timeit(badPairDetector3.is_bad_pair, number=1000000))
    print(timeit.timeit(badPairDetector3.is_bad_pair_v2, number=1000000))
    print(timeit.timeit(badPairDetector3.is_bad_pair_v3, number=1000000))


if __name__ == "__main__":
    main()