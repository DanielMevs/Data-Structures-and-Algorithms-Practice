from collections import defaultdict, deque


class Solution:
    def ladderLength(
            self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)    
            result += 1
            
        return 0