# Last updated: 23/5/2025, 11:06:42 am
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]], second=0) -> int:
        n = len(nums)
        
        right = []
        ret = 0
        mini = -1

        for num in nums:
            xnum = num ^ k
            if xnum > num:
                right.append(num)
            else:
                ret += num
                diff = num - (num ^ k)
                if mini == -1 or mini - (mini ^ k) > diff:
                    mini = num
        
        right.sort(key=lambda x: (x ^ k) - x)
        
        while len(right) > 1:
            ret += right.pop() ^ k
            ret += right.pop() ^ k

        new_ret = ret
        if right:
            ret += right[0]
            if mini != -1:
                new_ret -= mini
                new_ret += mini ^ k

                new_ret += right[0] ^ k
            else:
                new_ret += right[0]
        
        return max(new_ret, ret)