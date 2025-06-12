# Last updated: 12/6/2025, 5:48:07 am
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        m = len(flowerbed)

        index = 0

        while index < m and n > 0:
            if flowerbed[index] == 0 and prev == 0 and (index+1 == m or flowerbed[index+1] == 0):
                n -= 1
                prev = 1
            else: prev = flowerbed[index]
            index += 1
        
        return n <= 0