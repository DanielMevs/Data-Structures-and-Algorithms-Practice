class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # - Same prefix but word1's length
            # - is greater than word2's -> invalid
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}  # False=visited, True=current path
        result = []

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
                
            visited[c] = False
            result.append(c)
        
        for c in adj:
            # - Detected a loop
            if dfs(c):
                return ''
        
        result.reverse()
        return ''.join(result)