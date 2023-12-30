class Solution(object):
    
    def longestCommonPrefix(self, strs):
        """Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        """
        if len(strs) == 1:
            return strs.pop()
        
        prefixCounter = {}

        def get_common_prefix_score(word):
            prefix = ''
            for letter in word:
                prefix += letter
                prefixCounter[prefix] = prefixCounter.get(prefix, 0) + 1
            
            return

        for word in strs:
            get_common_prefix_score(word)



        maxPrefix = max(prefixCounter.values()) if prefixCounter else 0
        
        scores = prefixCounter.values()
        
        if (len(set(scores)) == 1 and not scores[-1]) or maxPrefix < len(strs):
            return ''

        
        prefixCounter = list(prefixCounter.items())


        sort_prefix = lambda k, v: (v, k)

        return max(prefixCounter, key=lambda tup: sort_prefix(tup[0], tup[1]))[0]