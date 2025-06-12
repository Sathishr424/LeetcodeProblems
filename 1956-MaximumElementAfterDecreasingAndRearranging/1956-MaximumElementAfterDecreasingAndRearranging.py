# Last updated: 12/6/2025, 5:39:45 am
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        n = len(arr)

        if arr[0] != 1: arr[0] = 1

        ans = 1

        for i in range(1, n):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1]+1
            
            ans = max(ans, arr[i])

        return ans
