# Last updated: 16/7/2025, 11:08:26 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumLength(self, nums: List[int], k) -> int:
        # nums = [random.randrange(1, 10**7 + 1) for _ in range(2 * 10**5)]
        n = len(nums)

        matches = [[] for _ in range(k)]
        for i in range(n):
            for j in range(i+1, n):
                curr = (nums[i] + nums[j]) % k
                # print(curr, (i, j, (nums[i], nums[j])))
                matches[curr].append((i, j))
        
        for i in range(k):
            matches[i].sort()
        
        dp = [[-1] * k for _ in range(n)]

        def rec(index, match):
            if index == n: return 0
            if dp[index][match] != -1: return dp[index][match]
            ans = 0
            r_index = bisect_left(matches[match], (index, index))
            
            # print(index, match, r_index, matches[match])
            while r_index < len(matches[match]) and (index == -1 or matches[match][r_index][0] == index):
                ans = cmax(ans, rec(matches[match][r_index][1], match) + 1)
                r_index += 1
            dp[index][match] = ans
            return ans
        
        # [print(row) for row in matches]
        # print(matches)

        ret = 0
        for i in range(k):
            ret = max(ret, rec(-1, i) + 1)
        # rec.cache_clear()
        return ret
        
    