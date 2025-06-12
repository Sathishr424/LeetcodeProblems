# Last updated: 12/6/2025, 5:43:08 am
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        x = 0
        for i in range(n):
            if arr[i] % 2 == 1:
                x += 1
                if x == 3: return True
            else:
                x = 0
        
        return False