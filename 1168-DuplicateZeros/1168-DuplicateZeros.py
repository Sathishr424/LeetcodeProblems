# Last updated: 12/6/2025, 5:43:47 am
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                del arr[n]
                i+=1
            i+=1
        """
        Do not return anything, modify arr in-place instead.
        """
        