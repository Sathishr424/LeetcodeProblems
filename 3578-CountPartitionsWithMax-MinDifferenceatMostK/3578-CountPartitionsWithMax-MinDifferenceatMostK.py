# Last updated: 9/6/2025, 4:11:29 am
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7

        n = len(nums)
        sl = SortedList()

        cnt = 0
        cnts = [1] * (n+1)
        ret = 0
        add = 1
        for i in range(n-1, -1, -1):
            sl.add(nums[i])

            while sl[-1] - sl[0] > k:
                add -= cnts[i+cnt+1]
                sl.remove(nums[i+cnt])
                cnt -= 1
            
            z = ret
            ret = (ret + add) % mod
            cnts[i] = ret
            add += z
            cnt += 1

        return ret