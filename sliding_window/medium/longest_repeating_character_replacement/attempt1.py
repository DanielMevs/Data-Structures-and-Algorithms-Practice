class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        window_size = 1
        right, left = 0, 0
        count = {}

        while right < len(s):
            count[s[right]] = count.get(count, 0) + 1
            if window_size - self.get_most_frequent_char_count(count) <= k:
                result += 1
                window_size += 1
                right += 1
            else:
                count[s[right]] = count.get(count, 0) - 1
                left += 1
                result -= 1
                window_size -= 1

        return result

    def get_most_frequent_char_count(self, count):
        return count[max(count, key=lambda x: count[x])]
    
print(Solution().get_most_frequent_char_count({'k': 8, 's': 0, 'w': 4}))
