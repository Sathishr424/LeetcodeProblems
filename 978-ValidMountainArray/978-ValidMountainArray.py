# Last updated: 12/6/2025, 5:45:03 am
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False

        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                break
        if i == 1: return False
        for j in range(i, n):
            if arr[j] >= arr[j-1]:
                return False
        
        return True