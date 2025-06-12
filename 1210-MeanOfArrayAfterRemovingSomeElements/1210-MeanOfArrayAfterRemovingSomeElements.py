# Last updated: 12/6/2025, 5:43:37 am
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        cnt = int(n * 0.05)
        total = 0
        for i in range(cnt, n-cnt):
            total += arr[i]
        return total / (n-cnt*2)
