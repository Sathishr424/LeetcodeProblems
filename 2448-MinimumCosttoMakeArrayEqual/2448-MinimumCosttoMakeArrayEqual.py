# Last updated: 18/7/2025, 4:38:13 pm
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        new_nums = []
        for i, num in enumerate(nums):
            new_nums.append((num, cost[i]))
        new_nums.sort()
        
        prefix = []
        s = 0

        for i in range(n):
            num, c = new_nums[i]

            if i != 0:
                diff = num - new_nums[i-1][0]
                prev_cost = new_nums[i-1][1]

                curr_cost = prev_cost * diff + (s - prev_cost) * diff
                prefix.append(prefix[-1] + curr_cost)
            else:
                prefix.append(0)

            s += c
        
        right_c = 0
        s = 0
        ret = inf

        for i in range(n-1, -1, -1):
            num, c = new_nums[i]

            if i != n-1:
                diff = new_nums[i+1][0] - num
                prev_cost = new_nums[i+1][1]

                curr_cost = prev_cost * diff + (s - prev_cost) * diff
                right_c += curr_cost

            ret = min(ret, prefix[i] + right_c)
            s += c

        return ret
        