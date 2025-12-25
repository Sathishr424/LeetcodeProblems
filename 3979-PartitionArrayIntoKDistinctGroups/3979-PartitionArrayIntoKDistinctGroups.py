# Last updated: 12/25/2025, 7:09:34 PM
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        uniq = defaultdict(int)

        for num in nums:
            uniq[num] += 1

        heap = [-val for val in uniq.values()]
        heapq.heapify(heap)
        
        max_group = -heap[0]
        while heap:
            # print(g, heap)
            later = []
            for i in range(n-1, n-k-1, -1):
                if not heap: return False
                el = -heapq.heappop(heap)
                if el > 1:
                    later.append(el - 1)
            for el in later:
                heapq.heappush(heap, -el)
        # print(heap)
        return True