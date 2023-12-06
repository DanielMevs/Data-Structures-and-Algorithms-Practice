class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        k = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        count = 0
        most_recent = -1
        for i in range(1, k + 1):
            if flowerbed[i-1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0 and i - 1 != most_recent:
                count += 1
                most_recent = i
           
        return True if count == n else False
        
flowerbed = [1,0,0,0,1,0,0]
print(Solution().canPlaceFlowers(flowerbed=flowerbed, n=2))