class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        prefixN = [0] * (n + 1)
        postfixY = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixN[i] = prefixN[i - 1]
            if customers[i - 1] == "N":
                prefixN[i] += 1
                
        for i in range(n - 1, -1, -1):
            postfixY[i] = postfixY[i + 1]
            if customers[i] == "Y":
                postfixY[i] += 1
        
        min_penalty, idx = float("inf"), 0

        for i in range(n + 1):
            penalty = prefixN[i] + postfixY[i]
            if penalty < min_penalty:
                min_penalty = penalty
                idx = i
        
        return idx