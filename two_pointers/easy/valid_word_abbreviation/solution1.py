class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # indices for word and abbr, respectively

        while j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = 10 * num + int(abbr[j])
                    j += 1

                i += num
                if i > len(word):
                    return False
            else:
                if i >= len(word) or abbr[j] != word[i]:
                    return False
                i, j = i + 1, j + 1

        return i == len(word)
