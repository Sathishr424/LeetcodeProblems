# Last updated: 25/10/2025, 6:51:07 am
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        k -= 1
        arr = []
        for i in range(1, n):
            arr.append(weights[i-1] + weights[i])
        
        arr.sort()

        return sum(arr[len(arr) - k:]) - sum(arr[:k])