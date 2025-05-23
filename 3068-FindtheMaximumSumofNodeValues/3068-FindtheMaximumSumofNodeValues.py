# Last updated: 23/5/2025, 11:01:24 am
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]], second=0) -> int:
        n = len(nums)
        
        left = []
        right = []

        for num in nums:
            xnum = num ^ k
            if xnum > num:
                right.append(num)
            else:
                left.append(num)
        
        left.sort(key=lambda x: x - (x ^ k))
        right.sort(key=lambda x: (x ^ k) - x)

        ret = 0
        for x in left:
            ret += x
        
        while len(right) > 1:
            ret += right.pop() ^ k
            ret += right.pop() ^ k

        new_ret = ret
        if right:
            ret += right[0]
            if left:
                new_ret -= left[0]
                new_ret += left[0] ^ k

                new_ret += right[0] ^ k
            else:
                new_ret += right[0]
        
        return max(new_ret, ret)