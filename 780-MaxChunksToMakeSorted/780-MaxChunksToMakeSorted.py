# Last updated: 12/6/2025, 5:46:53 am
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefixSum = []
        tot = 0
        prefixSum.append(tot)
        for num in range(n):
            tot += num
            prefixSum.append(tot)
        def rec(start):
            if start == n: return 0
            tot = 0
            for i in range(start, n):
                tot += arr[i]
                if abs(prefixSum[start] - prefixSum[i+1]) == tot:
                    return 1 + rec(i+1)
            return 1
        
        return rec(0)
        