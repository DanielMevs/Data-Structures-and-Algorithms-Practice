class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_size = 0
        left = 0
        count = {}

        for right in range(len(s)):

            count[s[right]] = 1 + count.get(s[right], 0)
            window_size = (right - left + 1)
            max_freq = self.get_most_freq_char_count(count)


            if window_size - max_freq > k:

                count[s[left]] -= 1
                left += 1

        window_size = (right - left + 1)

        return window_size

    def get_most_freq_char_count(self, count):
        return max(count.values())
    

    

print(Solution().characterReplacement("AABABBA", 1))

