# Last updated: 17/7/2025, 8:41:48 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        new_arr = []
        for i in range(n):
            new_arr.append((nums2[i], i))
        
        new_arr.sort(key=lambda x: -x[0])

        heap = []
        s = 0
        score = 0

        for i in range(k-1):
            s += nums1[new_arr[i][1]]
            heapq.heappush(heap, nums1[new_arr[i][1]])

        for i in range(k-1, n):
            m, index = new_arr[i]
            s += nums1[index]
            heapq.heappush(heap, nums1[index])
            if len(heap) > k:
                s -= heapq.heappop(heap)
            
            score = cmax(score, s * m)
        
        return score