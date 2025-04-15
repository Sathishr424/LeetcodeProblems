# Last updated: 16/4/2025, 3:45:57 am
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        
        def mergeSort(arr):
            nonlocal ret
            if len(arr) == 1: return
            mid = len(arr) // 2
            
            left = arr[:mid]
            right = arr[mid:]
            
            mergeSort(left)
            mergeSort(right)
            
            i = 0
            j = 0
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    arr[k] = left[i]
                    ret[left[i][1]] += j
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                ret[left[i][1]] += j
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        mergeSort([(num, i) for i, num in enumerate(nums)])
        return ret