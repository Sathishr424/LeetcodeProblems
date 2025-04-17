# Last updated: 17/4/2025, 7:35:30 pm
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Merge Sort
        n = len(nums1)

        relation = [0] * n

        for i, num in enumerate(nums2):
            relation[num] = i
        
        arr = []
        for num in nums1:
            arr.append(relation[num])

        smaller = [0] * n
        larger = [0] * n

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
            
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    arr[k] = left[i]
                    larger[left[i][1]] += len(right) - j
                    i += 1
                else:
                    arr[k] = right[j]
                    smaller[right[j][1]] += i
                    j += 1
                
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                arr[k] = right[j]
                smaller[right[j][1]] += i
                j += 1
                k += 1
        mergeSort([(num, i) for i, num in enumerate(arr)])
        ret = 0
        for i in range(n):
            ret += smaller[i] * larger[i]

        return ret