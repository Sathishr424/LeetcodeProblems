# Last updated: 12/6/2025, 5:35:52 am
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]], second=0) -> int:
        n = len(nums)
        
        right = -1
        left = -1
        right_cnt = 0

        ret = 0

        for num in nums:
            xnum = num ^ k
            if xnum > num:
                ret += xnum
                if right == -1 or xnum - num < (right ^ k) - right:
                    right = num
                right_cnt += 1
            else:
                ret += num
                if left == -1 or num - xnum < left - (left ^ k):
                    left = num

        new_ret = ret
        if right_cnt % 2:
            ret -= right ^ k
            ret += right

            if left != -1:
                new_ret -= left
                new_ret += left ^ k
            else:
                new_ret -= right ^ k
                new_ret += right
        
        return max(new_ret, ret)