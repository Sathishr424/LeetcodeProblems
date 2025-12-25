# Last updated: 12/25/2025, 7:10:22 PM
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = []
        
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                arr.append(-1)
            elif nums[i] < nums[i + 1]:
                arr.append(1)
            else:
                arr.append(0)
        n = len(arr)
        # print(arr)
        if arr[0] != 1: return False
        j = 0
        while j < n and arr[j] == 1:
            j += 1

        if j == n or arr[j] != -1: return False
        while j < n and arr[j] == -1:
            j += 1

        if j == n or arr[j] != 1: return False
        while j < n and arr[j] == 1:
            j += 1
        
        return j == n