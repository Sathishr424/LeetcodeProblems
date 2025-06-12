# Last updated: 12/6/2025, 5:50:16 am
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        arr = []
        
        for num in counts:
            heapq.heappush(arr, (counts[num], num))
            if len(arr) > k: heapq.heappop(arr)
        
        return [a[1] for a in arr]