import timeit

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_size = 0
        left = 0
        count = {}

        for right in range(len(s)):

            count[s[right]] = 1 + count.get(s[right], 0)
            window_size = right - left + 1

            if window_size - self.most_freq_char_count(count) > k:

                count[s[left]] -= 1
                left += 1

        return window_size

    def most_freq_char_count1(self, count):
        return max(count.values())
    
    def most_freq_char_count2(self, count):
        return count[max(count, key=count.get)]
    
sample = {'k': 8, 's': 0, 'w': 4}
time1 = timeit.timeit(lambda: Solution().most_freq_char_count1(sample), number=1000)
time2 = timeit.timeit(lambda: Solution().most_freq_char_count2(sample), number=1000)

print(f"Key as values prints after {time1} seconds")
print(f"Key as values prints after {time2} seconds")
    