# Last updated: 9/8/2025, 6:50:29 am
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

        l = 0
        r = 1
        add = 0.000000001
        numerator = 0
        denominator = 0
        
        while l < r:
            mid = (l + r) / 2
            
            count = 0
            nume = 0
            deno = 0
            # [1,13,17,59]
            for i in range(n-1):
                j = n-1
                while count < k and j > i and nums[i] / nums[j] <= mid:
                    if mid - (nums[i] / nums[j]) < abs(mid - (nums[nume] / nums[deno])):
                        nume = i
                        deno = j
                    j -= 1
                    count += 1

            # print((l, mid, r), count, (nume, deno))
            if count >= k:
                numerator = nume
                denominator = deno
                r = mid - add
            else:
                l = mid + add

        return [nums[numerator], nums[denominator]]

    
