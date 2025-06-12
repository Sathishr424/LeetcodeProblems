# Last updated: 12/6/2025, 5:39:15 am
class Solution:
    def longestObstacleCourseAtEachPosition(self, obs: List[int]) -> List[int]:
        arr = []
        ret = []
        for o in obs:
            j = bisect_right(arr,o)
            if j == len(arr): arr.append(o)
            else: arr[j] = o
            ret.append(j+1)
        return ret
        