# Last updated: 9/8/2025, 4:46:23 am
def maxHeap(nums, n, k):
    heap = []
    for i in range(n-1):
        heapq.heappush(heap, (-nums[i] / nums[i+1], i, i+1))

    for _ in range(k-1):
        _, i, j = heapq.heappop(heap)

        if j+1 < n:
            j += 1
            heapq.heappush(heap, (-nums[i] / nums[j], i, j))
    
    _, i, j = heapq.heappop(heap)
    return [nums[i], nums[j]]

def minHeap(nums, n, k):
    heap = []
    for i in range(n-1):
        heapq.heappush(heap, (nums[i] / nums[n-1], i, n-1))

    while k-1:
        _, i, j = heapq.heappop(heap)

        if j-1 > i:
            j -= 1
            heapq.heappush(heap, (nums[i] / nums[j], i, j))
        k -= 1
    
    _, i, j = heapq.heappop(heap)
    return [nums[i], nums[j]]

class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        n_k = (n * (n-1) // 2) - k + 1
        if n_k < k:
            return maxHeap(nums, n, n_k)
        
        return minHeap(nums, n, k)
    
