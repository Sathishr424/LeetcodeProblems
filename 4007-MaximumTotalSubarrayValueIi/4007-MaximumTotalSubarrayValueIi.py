# Last updated: 12/25/2025, 7:09:16 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        k_log = floor(log2(n)) + 1
        
        max_logs = [[0] * n for _ in range(k_log)]

        for i in range(n):
            max_logs[0][i] = nums[i]
    
        for power in range(1, k_log):
            m = 1 << power
            prev_m = m >> 1

            for i in range(n-m+1):
                max_logs[power][i] = max(max_logs[power - 1][i], max_logs[power - 1][i + prev_m])

        min_logs = [[0] * n for _ in range(k_log)]

        for i in range(n):
            min_logs[0][i] = nums[i]
    
        for power in range(1, k_log):
            m = 1 << power
            prev_m = m >> 1

            for i in range(n-m+1):
                min_logs[power][i] = min(min_logs[power - 1][i], min_logs[power - 1][i + prev_m])

        def getMin(l, r):
            dis = r - l + 1

            power = floor(log2(dis))
            m = 1 << power
            return min(min_logs[power][l], min_logs[power][r - m + 1])

        def getMax(l, r):
            dis = r - l + 1

            power = floor(log2(dis))
            m = 1 << power
            return max(max_logs[power][l], max_logs[power][r - m + 1])

        heap = []
        heapq.heappush(heap, (-(max(nums) - min(nums)), 0, n-1))

        used = {}
        ret = 0
        while k:
            maxi, l, r = heapq.heappop(heap)
            if (l, r) in used: continue
            used[(l, r)] = 1
            ret += -maxi
            k -= 1

            new_l = l
            new_r = r - 1
            if new_r >= new_l:
                maxi = getMax(new_l, new_r)
                mini = getMin(new_l, new_r)
                heapq.heappush(heap, (-(maxi - mini), new_l, new_r))
            
            new_l = l + 1
            new_r = r
            if new_r >= new_l:
                maxi = getMax(new_l, new_r)
                mini = getMin(new_l, new_r)
                heapq.heappush(heap, (-(maxi - mini), new_l, new_r))

        return ret