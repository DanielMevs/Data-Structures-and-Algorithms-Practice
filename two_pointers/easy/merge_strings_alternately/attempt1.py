class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            letters = [str(_) for _ in range(len(word1) + len(word2))]
            for i in range(len(word1)):
                if i*2 < len(letters):
                    letters[i*2] = word1[i]
            for i in range(len(word2)):
                if (i * 2) + 1 <= len(letters):
                    letters[(i*2)+1] = word2[i]
            return ''.join(letters)
        elif len(word1)< len(word2):
            letters = [str(i) for i in range(len(word1)*2)]
            remaining = []
            right = 0
            for i in range(len(letters)):
                if i*2 < len(letters):
                    letters[i*2] = word1[i]
                    right += 1
            for i in range(len(letters)):
                if (i * 2) + 1 <= len(letters):
                    letters[(i*2)+1] = word2[i]
            for i in range(right, len(word2)):
                remaining.append(word2[i])
            result = letters + remaining
            return ''.join(result)
        else:
            letters = [str(i) for i in range(len(word2)*2)]
            remaining = []
            right = 0
            for i in range(len(letters)):
                if i*2 < len(letters):
                    letters[i*2] = word1[i]
                    right += 1
            for i in range(len(letters)):
                if (i * 2) + 1 <= len(letters):
                    letters[(i*2)+1] = word2[i]
            for i in range(right, len(word1)):
                remaining.append(word1[i])
            result = letters + remaining
            return ''.join(result)
        