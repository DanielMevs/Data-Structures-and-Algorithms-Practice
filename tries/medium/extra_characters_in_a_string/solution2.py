from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in dp:
                return dp[i]

            result = 1 + dfs(i + 1)  # skip current character
            current = trie
            for j in range(i, len(s)):
                if s[j] not in current.children:
                    break
                current = current.children[s[j]]
                if current.word:
                    result = min(result, dfs(j + 1))
            dp[i] = result
            return result

        return dfs(0)
