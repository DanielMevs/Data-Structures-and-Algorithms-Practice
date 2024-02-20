class Solution:
    def suggestedProducts(
            self, products: list[str], searchWord: str) -> list[list[str]]:
        result = []
        products.sort()

        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            char = searchWord[i]

            while left <= right and \
                    (len(products[left]) <= i or
                        products[left][i] != char):
                left += 1
            while left <= right and \
                    (len(products[right]) <= i or
                        products[right][i] != char):
                right -= 1
            
            result.append([])
            remaining = right - left + 1
            for j in range(min(3, remaining)):
                result[-1].append(products[left + j])
            
        return result