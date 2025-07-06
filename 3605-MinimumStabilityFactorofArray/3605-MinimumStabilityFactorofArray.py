# Last updated: 6/7/2025, 7:40:50 am
class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)

        k = floor(log2(n)) + 1
        s_table = [[1] * n for _ in range(k)]

        for i in range(n):
            s_table[0][i] = nums[i]

        for power in range(1, k):
            m = 1 << power
            prev_m = m >> 1

            for i in range(n - m + 1):
                s_table[power][i] = gcd(s_table[power - 1][i], s_table[power - 1][i + prev_m])
        
        # [print(row) for row in s_table]

        l = 1
        r = n + 1

        while l < r:
            mid = (l + r) // 2
            # print((l, r), mid)
            
            power = floor(log2(mid))
            rem = maxC
            left = 0
            while left < (n - mid + 1):
                right = left + mid - 1
                curr = gcd(s_table[power][left], s_table[power][right - (1 << power) + 1])
                if curr >= 2:
                    rem -= 1
                    left += mid
                else:
                    left += 1
            # print(rem)
            if rem >= 0:
                r = mid
            else:
                l = mid + 1
        
        return l - 1
