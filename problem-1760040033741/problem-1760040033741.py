# Last updated: 10/10/2025, 1:30:33 am
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        new_arr = []
        for i in range(n):
            new_arr.append((nums2[i], i))

        new_arr.sort(reverse=True)
        heap = []
        s = 0

        for i in range(k):
            s += nums1[new_arr[i][1]]
            heapq.heappush(heap, nums1[new_arr[i][1]])
        # print(new_arr, s)
        best = s * new_arr[i][0]
        for i in range(k, n):
            s -= heapq.heappop(heap)
            s += nums1[new_arr[i][1]]
            heapq.heappush(heap, nums1[new_arr[i][1]])

            best = max(best, s * new_arr[i][0])

        return best