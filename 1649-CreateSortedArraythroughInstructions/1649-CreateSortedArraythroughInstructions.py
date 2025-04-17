# Last updated: 17/4/2025, 11:37:23 am
mod = 10 ** 9 + 7
class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        n = len(nums)
        smaller = [0] * n
        larger = [0] * n
        cost = 0

        def mergeSort(arr):
            if len(arr) == 1: return
            mid = len(arr) // 2
            
            left = arr[:mid]
            right = arr[mid:]
            
            mergeSort(left)
            mergeSort(right)

            i = 0
            j = 0
            k = 0
            cnt = 0
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    arr[k] = left[i]
                    if i > 0 and left[i][0] == left[i-1][0]: cnt += 1
                    else: cnt = 1
                    i += 1
                else:
                    arr[k] = right[j]
                    if i-1 >= 0 and left[i-1][0] == right[j][0]:
                        smaller[right[j][1]] += i-cnt
                    else:
                        smaller[right[j][1]] += i
                    larger[right[j][1]] += len(left) - i
                    j += 1
                
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                if i-1 >= 0 and left[i-1][0] == right[j][0]:
                    smaller[right[j][1]] += i-cnt
                else:
                    smaller[right[j][1]] += i
                j += 1
                k += 1
        mergeSort([(num, i) for i, num in enumerate(nums)])
        
        for i in range(n):
            cost = (cost + min(smaller[i], larger[i])) % mod

        return cost
            