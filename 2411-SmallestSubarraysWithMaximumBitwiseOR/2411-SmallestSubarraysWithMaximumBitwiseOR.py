# Last updated: 29/7/2025, 2:29:00 pm
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxi = 0
        for num in nums:
            maxi |= num
        
        # print(maxi)

        k = floor(log2(n)) + 1
        logs = [[0] * n for _ in range(k)]
        for i in range(n):
            logs[0][i] = nums[i]
        
        for power in range(1, k):
            m = 1 << power
            prev_m = m >> 1
            for i in range(n-m+1):
                logs[power][i] = logs[power - 1][i] | logs[power - 1][i + prev_m]

        def getOR(l, r):
            dis = r - l + 1
            power = floor(log2(dis))
            return logs[power][l] | logs[power][r - (1 << power) + 1]

        ret = [0] * n

        left = 0
        right = 0
        while left < n:
            maxi = getOR(left, n-1)
            while right + 1 < n and getOR(left, right) < maxi:
                right += 1

            # print(left, right, nums[left:right+1], getOR(left, right))
            ret[left] = right - left + 1
            left += 1
            right = max(right, left)
        
        return ret
        
