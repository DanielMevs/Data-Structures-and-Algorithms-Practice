class Solution(object):
    
    def longestCommonPrefix(self, strs):
        """Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        """
        if strs == ['']:
            return ''
        prefixCounter = {}

        def get_common_prefix_score(word):
            prefix = ''
            for letter in word:
                prefix += letter
                prefixCounter[prefix] = prefixCounter.get(prefix, 0) + 1
            
            return

        for word in strs:
            get_common_prefix_score(word)
        
        print(prefixCounter)
        
        max_prefix = max(prefixCounter.values())

        if max_prefix <= 1:
            return ''

        # print(max_prefix)

        prefixes = [key for key, val in prefixCounter.items() if val == max_prefix]

        # print(prefixes)

        return max(prefixes)