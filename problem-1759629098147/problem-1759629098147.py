# Last updated: 5/10/2025, 7:21:38 am
mod = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot = sum(nums)
        if tot // 2 < k: return 0

        s = 0
        prefix = [0]
        for i in range(n):
            s += nums[i]
            prefix.append(s)

        @cache
        def rec2(index, rem):
            if index == n: return 0

            ans = rec2(index + 1, rem)
            if rem - nums[index] <= 0:
                ans += pow(2, n - index - 1, mod)
            else:
                ans += rec2(index + 1, rem - nums[index])
            # print(index, rem, ans, 'rec2')
            return ans % mod

        @cache
        def rec(index, curr):
            if index == n: return 0
            ans = rec(index + 1, curr)
            s = nums[index] + curr
            if s >= k:
                if tot - s >= k:
                    left = prefix[index + 1] - s
                    if left >= k:
                        possible = n - index - 1
                        # print('perm', index, (s, left), possible, pow(2, possible, mod))
                        ans += pow(2, possible, mod)
                    else:
                        need = k - left
                        this = rec2(index + 1, need)
                        # print(index, s, need, this)
                        ans += this
            else:
                ans += rec(index + 1, s)
            # print(index, ans)
            return ans % mod

        ans = rec(0, 0)
        rec.cache_clear()
        rec2.cache_clear()
        return ans