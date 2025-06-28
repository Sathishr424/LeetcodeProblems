# Last updated: 28/6/2025, 9:10:49 am
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)

        sl = SortedList()
        for i in range(k):
            sl.add(nums[i])
        
        ret = []
        if k % 2:
            ret.append(sl[k // 2])
        else:
            ret.append((sl[k // 2] + sl[k // 2 - 1]) / 2)
        
        for i in range(k, n):
            sl.remove(nums[i-k])
            sl.add(nums[i])

            if k % 2:
                ret.append(sl[k // 2])
            else:
                ret.append((sl[k // 2] + sl[k // 2 - 1]) / 2)

        return ret