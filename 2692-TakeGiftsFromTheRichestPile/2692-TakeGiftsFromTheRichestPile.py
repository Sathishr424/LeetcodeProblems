# Last updated: 12/6/2025, 5:37:13 am
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        arr = []
        for gift in gifts:
            heapq.heappush(arr, -gift)
        
        ret = 0
        for i in range(k):
            val = heapq.heappop(arr) * -1
            heapq.heappush(arr, -int(math.sqrt(val)))
        # print(arr)
        return sum(arr) * -1