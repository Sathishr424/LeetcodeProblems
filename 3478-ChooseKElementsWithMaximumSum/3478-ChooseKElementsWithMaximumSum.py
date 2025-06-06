# Last updated: 6/6/2025, 6:44:58 pm
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        ret = [0] * n

        arr = []
        for i in range(n):
            arr.append((nums1[i], i))
        arr.sort(key=lambda x: x[0])

        heap = []
        total = 0

        for index in range(n):
            num, i = arr[index]

            if num == arr[index-1][0]:
                ret[i] = ret[arr[index-1][1]]
            else:
                ret[i] = total

            total += nums2[i]
            heapq.heappush(heap, nums2[i])

            if len(heap) > k:
                total -= heapq.heappop(heap)

        return ret