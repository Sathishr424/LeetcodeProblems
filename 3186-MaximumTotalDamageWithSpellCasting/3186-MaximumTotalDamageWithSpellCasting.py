# Last updated: 11/10/2025, 1:30:35 pm
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        power.sort()
        prefix = [0]
        for p in power:
            prefix.append(prefix[-1] + p)

        @cache
        def rec(index):
            if index >= n: return 0

            ans = rec(index + 1)
            left = bisect_left(power, power[index] + 1)
            right = bisect_right(power, power[index] + 2)
            # print(index, power[index], left, right)
            ans = max(ans, rec(right) + prefix[left] - prefix[index])
            return ans
        
        return rec(0)