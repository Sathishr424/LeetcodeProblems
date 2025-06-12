# Last updated: 12/6/2025, 5:45:23 am
def heapify(arr, i, n):
    left = i*2 + 1
    right = i*2 + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        return heapify(arr, largest, n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n//2 -1, -1, -1):
            heapify(nums, i, n)

        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]

            heapify(nums, 0, i)
        
        return nums