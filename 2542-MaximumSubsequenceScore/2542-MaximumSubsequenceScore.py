# Last updated: 17/7/2025, 8:39:16 pm
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        new_arr = []
        for i in range(n):
            new_arr.append((nums2[i], i))
        
        new_arr.sort(key=lambda x: x[0])

        heap = []
        s = 0
        ret = 0
        for i in range(n-1, -1, -1):
            m, index = new_arr[i]
            s += nums1[index]
            heapq.heappush(heap, nums1[index])
            if len(heap) > k:
                s -= heapq.heappop(heap)
            
            if len(heap) == k:
                ret = max(ret, s * m)
        
        return ret