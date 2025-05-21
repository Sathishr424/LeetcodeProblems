# Last updated: 22/5/2025, 1:30:34 am
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        # [1, 4, 11], [2, 6, 7]
        heap = []

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited = {}
        ret = []

        while k:
            s, l, r = heapq.heappop(heap)
            key = l*n + r
            if key in visited: continue
            ret.append([nums1[l], nums2[r]])
            visited[key] = 1
            if r+1 < n:
                heapq.heappush(heap, (nums1[l] + nums2[r+1], l, r+1))
            elif l+1 < m:
                heapq.heappush(heap, (nums1[l+1] + nums2[r], l+1, r))
            
            if l+1 < m:
                heapq.heappush(heap, (nums1[l+1] + nums2[r], l+1, r))
            elif r+1 < n:
                heapq.heappush(heap, (nums1[l] + nums2[r+1], l, r+1))
            
            k -= 1
        
        return ret