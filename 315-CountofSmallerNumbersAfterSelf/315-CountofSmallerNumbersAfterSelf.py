# Last updated: 8/4/2025, 9:33:07 am
def mergeSort(nums):
    if len(nums) == 1: return
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    mergeSort(left)
    mergeSort(right)
    
    l = 0
    k = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l][0] > right[r][0]:
            nums[k] = right[r]
            r += 1
        else:
            nums[k] = left[l]
            nums[k][1] += r
            l += 1
        k += 1
    
    while l < len(left):
        nums[k] = left[l]
        nums[k][1] += r
        l += 1
        k += 1
    
    while r < len(right):
        nums[k] = right[r]
        r += 1
        k += 1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        arr = []
        for i, num in enumerate(nums):
            arr.append([num, 0, i])

        mergeSort(arr)
        ret = [0] * n

        for _, cnt, index in arr:
            ret[index] = cnt
        return ret