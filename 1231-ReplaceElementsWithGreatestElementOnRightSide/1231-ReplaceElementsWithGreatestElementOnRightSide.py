# Last updated: 12/6/2025, 5:43:28 am
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prev = arr[n-1]
        arr[n-1] = -1
        for i in range(n-1, 0, -1):
            prev, arr[i-1] = arr[i-1], max(arr[i], prev)
        return arr