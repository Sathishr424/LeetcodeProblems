# Last updated: 18/7/2025, 4:41:11 pm
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        new_nums = []
        for i, num in enumerate(nums):
            new_nums.append((num, cost[i]))
        new_nums.sort()
        
        prefix = [0]
        s = new_nums[0][1]

        for i in range(1, n):
            num, c = new_nums[i]

            diff = num - new_nums[i-1][0]
            prev_cost = new_nums[i-1][1]

            curr_cost = prev_cost * diff + (s - prev_cost) * diff
            prefix.append(prefix[-1] + curr_cost)

            s += c
        
        right_c = 0
        s = new_nums[n-1][1]
        ret = prefix[n-1]

        for i in range(n-2, -1, -1):
            num, c = new_nums[i]

            diff = new_nums[i+1][0] - num
            prev_cost = new_nums[i+1][1]

            curr_cost = prev_cost * diff + (s - prev_cost) * diff
            right_c += curr_cost

            ret = min(ret, prefix[i] + right_c)
            s += c

        return ret
        