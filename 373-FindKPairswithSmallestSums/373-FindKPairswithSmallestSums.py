# Last updated: 22/9/2025, 10:47:16 pm
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        nums1.sort()
        nums2.sort()

        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        ret = []
        used = {}
        while k:
            _, i, j = heapq.heappop(heap)
            if (i, j) in used: continue
            used[(i, j)] = 1

            ret.append([nums1[i], nums2[j]])

            if i + 1 < n:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            if j + 1 < m:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return ret
