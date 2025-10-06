# Last updated: 6/10/2025, 7:11:35 pm
from functools import cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        nums = list(map(int, str(n)))
        m = len(nums)

        @cache
        def rec(pos: int, mask: int, tight: bool, leading: bool) -> int:
            if pos == m:
                # One valid number formed (including all-zero if leading=True)
                return 0 if leading else 1

            ans = 0
            limit = nums[pos] if tight else 9

            for d in range(0, limit + 1):
                new_tight = tight and (d == limit)

                if leading and d == 0:
                    # Still leading zeros, no digit used
                    ans += rec(pos + 1, mask, new_tight, True)
                else:
                    if (mask >> d) & 1:
                        # Repeated digit — skip
                        continue
                    ans += rec(pos + 1, mask | (1 << d), new_tight, False)

            return ans

        unique_count = rec(0, 0, True, True)
        return n - unique_count
