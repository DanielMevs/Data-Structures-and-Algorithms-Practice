class Solution:
    def maxProduct(self, s: str) -> int:
        N, pali = len(s), {} # bitmask: length
         
        for mask in range(1, 1 << N): # 1 << N == 2 ** N
            subseq = ''
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq ==subseq[::-1]:
                pali[mask] = len(subseq)
        
        # - To determine the length of our longest disjoint subsequence
        result = 0
        for m1 in pali:
            for m2 in pali:
                # - Disjoint
                if m1 & m2 == 0:
                    result = max(result, pali[m1] * pali[m2] )
        
        return result

