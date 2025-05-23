# Last updated: 23/5/2025, 10:59:48 am
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]], second=0) -> int:
        n = len(nums)
        
        left = []
        right = []

        for num in nums:
            xnum = num ^ k
            if xnum > num:
                right.append((num, xnum))
            else:
                left.append((num, xnum))
        
        left.sort(key=lambda x: x[0] - x[1])
        right.sort(key=lambda x: x[1] - x[0])

        ret = 0
        for x, _ in left:
            ret += x
        
        while len(right) > 1:
            ret += right.pop()[1]
            ret += right.pop()[1]

        new_ret = ret
        if right:
            ret += right[0][0]
            if left:
                new_ret -= left[0][0]
                new_ret += left[0][1]

                new_ret += right[0][1]
            else:
                new_ret += right[0][0]
        
        return max(new_ret, ret)