# Last updated: 27/5/2025, 4:38:04 pm
class Solution:
    def minCost(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6 7
        # 1 2 3
        n = len(nums)
        if n < 3: return max(nums)
        
        memo = [[-1] * (n+1) for _ in range(n+1)]

        def dfs(index, prev_index):
            if memo[index][prev_index] != -1: return memo[index][prev_index]
            if n-index < 2:
                return max([nums[prev_index]] + nums[index:])
            
            one = dfs(index+2, index) + max(nums[prev_index], nums[index+1])
            two = dfs(index+2, prev_index) + max(nums[index], nums[index+1])
            three = dfs(index+2, index+1) + max(nums[prev_index], nums[index])
            ans = min(one, two, three)
            memo[index][prev_index] = ans
            return ans
    
        one = dfs(3, 0) + max(nums[1], nums[2])
        two = dfs(3, 1) + max(nums[0], nums[2])
        three = dfs(3, 2) + max(nums[0], nums[1])

        return min(one, two, three)