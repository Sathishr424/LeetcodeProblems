# Last updated: 11/5/2025, 7:55:46 am
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False

        for i in range(n-2):
            if arr[i] % 2 and arr[i+1] % 2 and arr[i+2] % 2: return True
        
        return False